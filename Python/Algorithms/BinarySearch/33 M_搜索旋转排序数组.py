# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 33 搜索旋转排序数组
# @Content : 整数数组 nums 按升序排列，数组中的值 互不相同 。
#            在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为
#            [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
#            例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#            给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[0] <= nums[mid] and (target > nums[mid] or target < nums[0]):
                low = mid + 1
            elif target > nums[mid] and target < nums[0]:
                low = mid + 1
            else:
                high = mid
        return low if low == high and target == nums[low] else -1


if __name__ == '__main__':
    # case1  res = 4
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 4

    # case2  res = -1
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3

    # case3  res = -1
    nums3 = [1]
    target3 = 0

    sol = Solution()
    res1 = sol.search(nums1, target1)
    res2 = sol.search(nums2, target2)
    res3 = sol.search(nums3, target3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)