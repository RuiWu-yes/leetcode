# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 88 合并两个有序数组
# @Content : 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#            初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，
#            这样它就有足够的空间保存来自 nums2 的元素。
from typing import List


class Solution:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 合并后排序 O((n+m)log(n+m))
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 双指针(需要临时数组res)
        res = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                res.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                res.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        nums1[:] = res

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 逆向双指针(原地修改)
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:  # nums1已经到遍历完成
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:  # nums2已经遍历完成
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == '__main__':
    # case1  res = [1, 2, 2, 3, 5, 6]
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()
    sol.merge1(nums1, m, nums2, n)
    # sol.merge2(nums1, m, nums2, n)
    # sol.merge3(nums1, m, nums2, n)
    print('case1:', nums1)