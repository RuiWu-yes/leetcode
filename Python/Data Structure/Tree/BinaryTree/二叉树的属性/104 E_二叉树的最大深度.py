# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 104 二叉树的最大深度
# @Content : 给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# @Explain : 叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        # 递归法
        if not root: return 0
        height_left = self.maxDepth1(root.left)
        height_right = self.maxDepth1(root.right)
        return max(height_left, height_right) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        # 迭代法
        # 层序遍历
        if not root: return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return depth


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 3
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1_1, res1_2 = sol.maxDepth1(root1), sol.maxDepth2(root1)
    print('case1:', res1_1, res1_2)