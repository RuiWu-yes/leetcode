# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 108 将有序数组转换为二叉搜索树
# @Content : 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
#            高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 递归法
        def traversal(left, right):
            if left > right: return
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])              # 根：有序数组的中间元素
            root.left = traversal(left, mid - 1)    # 左
            root.right = traversal(mid + 1, right)  # 右
            return root
        return traversal(0, len(nums) - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        # 迭代法
        if not nums: return
        root = TreeNode()
        queue = [[root, 0, len(nums)-1]]
        while queue:
            curNode, left, right = queue.pop(0)
            mid = left + (right - left) // 2
            curNode.val = nums[mid]  # 将mid对应的元素给中间节点
            if left < mid:   # 处理左区间
                curNode.left = TreeNode()
                queue.append([curNode.left, left, mid-1])
            if right > mid:  # 处理右区间
                curNode.right = TreeNode()
                queue.append([curNode.right, mid+1, right])
        return root


if __name__ == '__main__':
    # case1  res = [0, -3, 9, -10, None, 5]
    # 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案
    nums1 = [-10, -3, 0, 5, 9]

    # case2  res = [3, 1]
    # 解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树
    nums2 = [1, 3]

    sol = Solution()
    root1_0, root1_1 = sol.sortedArrayToBST(nums1), sol.sortedArrayToBST1(nums1)
    root2_0, root2_1 = sol.sortedArrayToBST(nums2), sol.sortedArrayToBST1(nums2)

    from libs.tree import BinaryTree as BT
    res1_0, res1_1 = BT().inorder(root1_0), BT().inorder(root1_1)
    res2_0, res2_1 = BT().inorder(root2_0), BT().inorder(root2_1)
    print('case1:', res1_0, res1_1)
    print('case2:', res2_0, res2_1)