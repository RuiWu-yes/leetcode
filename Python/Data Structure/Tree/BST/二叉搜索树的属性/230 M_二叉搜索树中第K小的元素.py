# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 230 二叉搜索树中第K小的元素
# @Content : 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# @explain : 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 递归法
        # BST按中序遍历是有序的
        res, rank = 0, 0  # res记录结果； rank记录当前元素排名
        def traverse(root, k):
            nonlocal res, rank
            if not root: return
            traverse(root.left, k)   # 左
            # 中序遍历代码位置          # 根
            rank += 1
            if rank == k:
                # 找到第k小元素
                res = root.val
                return
            traverse(root.right, k)  # 右
        traverse(root, k)
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # case1  res = 1
    # 输入：
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    list1 = [3, 1, 4, None, 2]
    Tree = ListCreateTree()
    root1 = Tree.lct(None, list1, 0)
    k1 = 1

    # case2  res = 3
    # 输入：
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    list2 = [5, 3, 6, 2, 4, None, None, 1]
    Tree = ListCreateTree()
    root2 = Tree.lct(None, list2, 0)
    k2 = 3

    sol = Solution()
    res1 = sol.kthSmallest(root1, k1)
    res2 = sol.kthSmallest(root2, k2)
    print('case1: ', res1)
    print('case2: ', res2)