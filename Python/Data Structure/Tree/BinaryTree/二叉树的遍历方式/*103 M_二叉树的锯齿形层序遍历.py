# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 103 二叉树的锯齿形层序遍历
# @Content : 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        # 迭代法
        res = []
        if not root: return res
        queue = [root]
        depth = 0
        while queue:
            child = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                child.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2 == 1:
                res.append(child[::-1])
            else:
                res.append(child)
            depth += 1
        return res

    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        # 递归法
        res = []
        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res