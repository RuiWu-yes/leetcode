# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 515 在每个树行中找最大值
# @Content : 您需要在二叉树的每一行中找到最大的值。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # BFS
        res = []
        if not root: return res
        deque = [root]
        while deque:
            child = []
            for _ in range(len(deque)):
                node = deque.pop(0)
                child.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(max(child))
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = [1, 3, 9]
    #           1
    #          / \
    #         3   2
    #        / \   \
    #       5   3   9
    list1 = [1, 3, 2, 5, 3, None, 9]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1 = sol.largestValues(root1)
    print('case1:', res1)