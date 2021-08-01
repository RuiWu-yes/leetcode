# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 145 二叉树的后序遍历
# @Content : 给定一个二叉树，返回它的 后序 遍历。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归法(后序遍历：左右根)
        res = []
        def traversal(root):
            if not root: return
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)
        traversal(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        # 递归法(后序遍历：左右根)
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]