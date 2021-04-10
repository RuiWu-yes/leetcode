# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 144 二叉树的前序遍历
# @Content : 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归法(前序遍历：根左右)
        res = []
        def traversal(root):
            if not root: return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代法(前序遍历：根左右)
        res = []
        if not root: return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res