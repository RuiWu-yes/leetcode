# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 153 寻找旋转排序数组中的最小值
# @Content : 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
#            请找出其中最小的元素。
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分法
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    # case1  res = 1
    nums1 = [3, 4, 5, 1, 2]

    # case2  res = 0
    nums2 = [4, 5, 6, 7, 0, 1, 2]

    # case3  res = 1
    nums3 = [1]

    sol = Solution()
    res1 = sol.findMin(nums1)
    res2 = sol.findMin(nums2)
    res3 = sol.findMin(nums3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)