# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 257 二叉树的所有路径
# @Content : 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# @Explain : 叶子节点是指没有子节点的节点。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        # 递归法
        # 前序遍历（回溯）
        if not root: return []
        res = []
        def traversal(cur, path):
            path += str(cur.val)  # 根
            # 递归终止条件：左右节点都为空(到达叶子节点)
            if not cur.left and not cur.right:
                res.append(path)
                return
            if cur.left: traversal(cur.left, path + "->")  # 左
            if cur.right: traversal(cur.right, path + "->")  # 右
        traversal(root, "")
        return res

    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        # 迭代法
        if not root: return []
        res = []
        stack = [[root, str(root.val)]]
        while stack:
            node, path = stack.pop()  # 根
            if not node.left and not node.right:
                res.append(path)
            if node.right:  # 右
                stack.append([node.right, path + "->" + str(node.right.val)])
            if node.left:   # 左
                stack.append([node.left, path + "->" + str(node.left.val)])
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = ["1->2->5", "1->3"]
    # 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
    #    1
    #  /   \
    # 2     3
    #  \
    #   5
    list1 = [1, 2, 3, None, 5]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1_1, res1_2 = sol.binaryTreePaths1(root1), sol.binaryTreePaths2(root1)
    print('case1:', res1_1, res1_2)