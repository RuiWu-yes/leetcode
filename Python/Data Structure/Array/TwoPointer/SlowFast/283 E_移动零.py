# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 283 移动零
# @Content : 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# @Explain : 1) 必须在原数组上操作，不能拷贝额外的数组。
#            2) 尽量减少操作次数。


class Solution:
    def moveZeroes1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快慢指针
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # 将 slow与之后的所有元素赋值为 0
        for i in range(slow, len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count] = nums[i]
        for j in range(len(nums)-count, len(nums)):
            nums[j] = 0


if __name__ == '__main__':
    # case1  res = [1, 3, 12, 0, 0]
    nums1 = [0, 1, 0, 3, 12]
    nums2 = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes1(nums1)
    sol.moveZeroes2(nums2)
    print(nums1)
    print(nums2)