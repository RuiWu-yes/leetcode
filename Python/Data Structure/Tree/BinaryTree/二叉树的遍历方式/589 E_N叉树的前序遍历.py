# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 589 N叉树的前序遍历
# @Content : 给定一个 N 叉树，返回其节点值的 前序遍历 。
#            N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
#      进阶 ：递归法很简单，你可以使用迭代法完成此题吗?
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归法
        # 前序遍历(根左右)
        res = []
        if not root: return res
        res.append(root.val)         # 根
        for child in root.children:  # 左--右
            res.extend(self.preorder(child))
        return res

    def preorder1(self, root: 'Node') -> List[int]:
        # 迭代法
        # 前序遍历(根左右)
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)  # 根
            stack.extend(node.children[::-1])  # 栈(右--左) --> 出栈(左--右)
        return res