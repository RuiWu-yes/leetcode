# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 111 二叉树的最小深度
# @Content : 给定一个二叉树，找出其最小深度。
#            最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#            说明：叶子节点是指没有子节点的节点。
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS
        if not root: return 0
        depth = 1
        deque = collections.deque([root])
        while deque:
            for _ in range(len(deque)):
                node = deque.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 2
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1 = sol.minDepth(root1)
    print('case1:', res1)