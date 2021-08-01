# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 162 寻找峰值
# @Content : 峰值元素是指其值大于左右相邻值的元素。
#            给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#            你可以假设 nums[-1] = nums[n] = -∞ 。
from typing import List


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        # 暴力法 O(N)
        nums = [float("-inf")] + nums + [float("-inf")]
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i - 1

    def findPeakElement2(self, nums: List[int]) -> int:
        # 二分法 O(log(N))
        # 1) 首先要注意题目条件，在题目描述中出现了 nums[-1] = nums[n] = -∞，这就代表着 只要数组中存在一个元素比相邻元素大，那么沿着它一定可以找到一个峰值
        # 2) 根据上述结论，我们就可以使用二分查找找到峰值
        # 3) 查找时，左指针 left，右指针 right，以其保持左右顺序为循环条件
        # 4) 根据左右指针计算中间位置 mid，并比较 mid 与 mid+1 的值，
        #    a) 如果 mid 较大，则左侧存在峰值，right = mid
        #    b) 如果 mid + 1 较大，则右侧存在峰值，left = mid + 1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    # case1  res = 2
    # 解释：3 是峰值元素，你的函数应该返回其索引 2
    nums1 = [1, 2, 3, 1]

    # case2  res = 1 or 5
    # 解释：你的函数可以返回索引 1，其峰值元素为 2；
    #      或者返回索引 5， 其峰值元素为 6。
    nums2 = [1, 2, 1, 3, 5, 6, 4]

    sol = Solution()
    res1 = sol.findPeakElement1(nums1), sol.findPeakElement2(nums1)
    res2 = sol.findPeakElement1(nums2), sol.findPeakElement2(nums2)
    print('case1:', res1)
    print('case2:', res2)