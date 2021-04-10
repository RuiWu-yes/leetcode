# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 704 二分查找
# @Content : 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，
#            写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    # case1  res = 4
    # 解释: 9 出现在 nums 中并且下标为 4
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9

    # case2  res = -1
    # 解释: 2 不存在 nums 中因此返回 -1
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2

    sol = Solution()
    res1 = sol.search(nums1, target1)
    res2 = sol.search(nums2, target2)
    print('case1:', res1)
    print('case2:', res2)