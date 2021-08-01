# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 合并k个有序数组
# @Content : 有k个长度可能不同的有序数组，将其合并成一个有序数组
from typing import List
import heapq


class Solution1:
    # 思路一： 快速排序思路
    def findmedian(self, nums: List[int]) -> int or float:
        if not nums: return 0

        n = len(nums)
        if n % 2 == 0:  # 数组有偶数个元素
            a = self.partition(nums, n // 2, 0, n - 1)
            b = self.partition(nums, n // 2 - 1, 0, n - 1)
            mid = (nums[a] + nums[b]) / (2 * 1.0)
            return mid
        else:           # 数组有奇数个元素
            mid = self.partition(nums, n // 2, 0, n - 1)
            return nums[mid]

    def partition(self, nums, k, start, end):
        key = nums[start]
        left, right = start, end

        while left < right:
            while left < right and nums[right] > key:
                right = right - 1
            nums[left] = nums[right]

            while left < right and nums[left] < key:
                left = left + 1
            nums[right] = nums[left]

        nums[left] = key

        if left == k:
            return left
        elif left > k:
            return self.partition(nums, k, start, left - 1)
        else:
            return self.partition(nums, k, left + 1, end)


class Solution2:
    # 思路二： 小顶堆
    # 思路如下：
    #    1) 取前 len(nums)/2 个元素建立小顶堆。可以知道堆顶元素是前 len(nums)/2 个元素中最小的。
    #    2) 从第 len(nums)/2+1 个元素开始，依次将其与堆顶元素比较。若比对顶元素大，则替换之，并调整堆。
    #    3) 数组剩下的所有元素比较完后，可以输出中位数。数组长度为奇数时，输出堆顶元素即可。数组长度为偶数时，输出堆顶元素与它的孩子结点中较小的那个的均值。
    def findmedian(self, nums: List[int]) -> int or float:
        size = len(nums) // 2 + 1
        heap = nums[:size]
        heapq.heapify(heap)
        for i in range(size, len(nums)):
            if heap[0] < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0] if len(nums) % 2 else (heapq.heappop(heap) + heap[0]) / 2.0


if __name__ == '__main__':
    # case1  res = 4
    nums1 = [3, 8, 1, 2, 0, 4, 5, 7, 6]

    # case2  res = 4.5
    nums2 = [3, 8, 1, 2, 0, 9, 4, 5, 7, 6]

    sol1, sol2 = Solution1(), Solution2()
    res1 = sol1.findmedian(nums1), sol2.findmedian(nums1)
    res2 = sol1.findmedian(nums2), sol2.findmedian(nums2)
    print('case1:', res1)
    print('case2:', res2)