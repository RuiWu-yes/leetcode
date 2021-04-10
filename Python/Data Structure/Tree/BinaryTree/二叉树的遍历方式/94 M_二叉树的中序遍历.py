# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 94 二叉树的中序遍历
# @Content : 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        # 递归法(中序遍历：左根右)
        res = []
        def traversal(root):
            if not root: return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代法(中序遍历：左根右)
        res, stack = [], []
        while root or stack:
            # 先把所有的从根开始的左子树的根节点压入栈中(左根)，后逐层又添加当前层的右节点
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()  # 当前子树的根节点
            res.append(root.val)
            root = root.right  # 当前左子树的右孩子节点(右)
        return res