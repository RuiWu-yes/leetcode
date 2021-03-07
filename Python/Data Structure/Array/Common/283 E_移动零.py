# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 283 移动零
# @Content : 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#      说明 : 1.必须在原数组上操作，不能拷贝额外的数组。
#            2.尽量减少操作次数。
from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        for j in range(len(nums) - count, len(nums)):
            nums[j] = 0

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    # case1  res = [1, 3, 12, 0, 0]
    nums1 = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes1(nums1)
    # sol.moveZeroes2(nums1)
    print('case1:', nums1)