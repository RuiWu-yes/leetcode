# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 590 N叉树的后序遍历
# @Content : 给定一个 N 叉树，返回其节点值的 后序遍历 。
#            N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
#      进阶 ：递归法很简单，你可以使用迭代法完成此题吗?
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 递归法
        # 后序遍历(左--右根)
        res = []
        if not root: return res
        for child in root.children:  # 左--右
            res.extend(self.postorder(child))
        res.append(root.val)         # 根
        return res

    def postorder1(self, root: 'Node') -> List[int]:
        # 迭代法
        # 后序遍历(左--右根)
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)  # 根
            if node.children:     # 栈(左--右) --> 出栈(右--左)
                stack.extend(node.children)
        return res[::-1]          # 根右--左 --> 左--右根