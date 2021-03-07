# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 429 N叉树的层序遍历
# @Content : 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
#            树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 层序遍历
        if not root: return []
        res = []
        deque = [root]
        while deque:
            child = []
            for _ in range(len(deque)):
                node = deque.pop(0)
                child.append(node.val)
                deque.extend(node.children)
            res.append(child)
        return res