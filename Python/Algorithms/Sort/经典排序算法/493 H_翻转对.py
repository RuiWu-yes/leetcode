# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 493 翻转对
# @Content : 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#            你需要返回给定数组中的重要翻转对的数量。
from typing import List
import bisect


class Solution:
    def reversePairs1(self, nums: List[int]) -> int:
        # 二分查找
        tb, res = [], 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2 * n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res


    def reversePairs2(self, nums: List[int]) -> int:
        # 归并排序 + 归并的同时统计
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(nums, l, mid, r) + left + right

    def merge(self, nums, l, mid, r):
        ans = 0
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            # i这个指针指的一直都是刚刚大于2倍nums[j]的元素，因为j所在的nums[mid+1, r]有序
            # 所以我们可以记录上一次的i，这样i最多也只从l到mid遍历一次
            while i <= mid and (nums[i] + 1) >> 1 <= nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache[c] = nums[t]
                c += 1
                t += 1
            cache[c] = nums[j]
            c += 1
            ans += mid - i + 1
        while t <= mid:
            cache[c] = nums[t]
            c += 1
            t += 1
        nums[l:r + 1] = cache
        return ans



if __name__ == '__main__':
    # case1  res = 2
    nums1 = [1, 3, 2, 3, 1]

    # case2  res = 1
    nums2 = [2, 4, 3, 5, 1]

    sol = Solution()
    res1 = sol.reversePairs(nums1)
    res2 = sol.reversePairs(nums2)
    print('case1:', res1)
    print('case2:', res2)