# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 654 最大二叉树
# @Content : 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#            1.二叉树的根是数组中的最大元素。
#            2.左子树是通过数组中最大值左边部分构造出的最大二叉树。
#            3.右子树是通过数组中最大值右边部分构造出的最大二叉树。
#            通过给定的数组构建最大二叉树，并且输出这个树的根节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        def build(nums, lo, hi):
            # base case
            if lo > hi: return
            index, maxVal = -1, float('-inf')
            # 找到数组中的最大值和对应的索引
            for i in range(lo, hi+1):
                if maxVal < nums[i]:
                    index = i
                    maxVal = nums[i]
            root = TreeNode(maxVal)
            # 递归调用构造左右子树
            root.left = build(nums, lo, index - 1)
            root.right = build(nums, index + 1, hi)
            return root
        return build(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    from libs.tree import BinaryTree as BT

    # case1
    # 输入：[3, 2, 1, 6, 0, 5]
    nums = [3, 2, 1, 6, 0, 5]
    # 输出：返回下面这棵树的根节点：[6, 3, 5, null, 2, 0, null, null, 1]
    #       6
    #     /   \
    #    3     5
    #     \    /
    #      2  0
    #        \
    #         1
    sol = Solution()
    root = sol.constructMaximumBinaryTree(nums)
    res = BT().inorder(root)
    print(res)