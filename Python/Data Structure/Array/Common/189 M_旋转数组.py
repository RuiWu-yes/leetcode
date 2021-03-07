# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 189 旋转数组
# @Content : 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#      进阶 ：1) 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#            2) 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == '__main__':
    # case1  res = [5, 6, 7, 1, 2, 3, 4]
    # 解释:
    # 向右旋转 1 步: [7,1,2,3,4,5,6]
    # 向右旋转 2 步: [6,7,1,2,3,4,5]
    # 向右旋转 3 步: [5,6,7,1,2,3,4]
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3

    # case2  res = [3, 99, -1, -100]
    # 解释:
    # 向右旋转 1 步: [99,-1,-100,3]
    # 向右旋转 2 步: [3,99,-1,-100]
    nums2 = [-1, -100, 3, 99]
    k2 = 2

    sol = Solution()
    res1 = sol.rotate(nums1, k1)
    res2 = sol.rotate(nums2, k2)
    print('case1:', res1)
    print('case2:', res2)