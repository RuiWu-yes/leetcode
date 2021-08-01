# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 169 多数元素|求众数
# @Content : 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
#            你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#       进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
from typing import List
from collections import Counter


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        # 哈希表
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums: List[int]) -> int:
        # 排序
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement3(self, nums: List[int]) -> int:
        # 分治算法
        def majority_element_rec(lo, hi):
            # 数组只有一个元素时候，直接返回这个元素
            if lo == hi: return nums[lo]
            # 递归左右两边
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)
            # 如果两部分是众数，则返回它。
            if left == right:
                return left
            # 否则，记录左右，比比较，较大者为众数
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right
        return majority_element_rec(0, len(nums)-1)

    def majorityElement4(self, nums: List[int]) -> int:
        # 摩尔投票法(时间复杂度：O(N), 空间复杂度：O(1))
        major = nums[0]
        count = 1
        del nums[0]
        for i in nums:
            if count == 0:
                count += 1
                major = i
            elif major == i:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    # case1  res = 3
    nums1 = [3, 2, 3]

    # case2  res = 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]

    sol = Solution()
    res1 = sol.majorityElement1(nums1), sol.majorityElement2(nums1), sol.majorityElement3(nums1), sol.majorityElement4(nums1)
    res2 = sol.majorityElement1(nums2), sol.majorityElement2(nums2), sol.majorityElement3(nums2), sol.majorityElement4(nums2)
    print('case1:', res1)
    print('case2:', res2)