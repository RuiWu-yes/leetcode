# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 15 三数之和
# @Content : 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
#            请你找出所有和为 0 且不重复的三元组。
#       注意：答案中不可以包含重复的三元组。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序 + 双指针 (O(NlogN) + O(N2))
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    # case1  res = [[-1, -1, 2], [-1, 0, 1]]
    nums1 = [-1, 0, 1, 2, -1, -4]

    # case2  res = []
    nums2 = []

    # case3  res = []
    nums3 = []

    sol = Solution()
    res1 = sol.threeSum(nums1)
    res2 = sol.threeSum(nums2)
    res3 = sol.threeSum(nums3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)