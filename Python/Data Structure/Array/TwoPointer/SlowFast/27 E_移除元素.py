# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 27 移除元素
# @Content : 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#            不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#            元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeElement(self, nums, val: int) -> int:
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    # case1  res = 2
    # 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
    # 你不需要考虑数组中超出新长度后面的元素。
    nums1 = [3, 2, 2, 3]
    val1 = 3

    # case2  res = 5
    # 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
    # 注意这五个元素可为任意顺序。
    # 你不需要考虑数组中超出新长度后面的元素。
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2

    sol = Solution()
    res1 = sol.removeElement(nums1, val1)
    res2 = sol.removeElement(nums2, val2)
    print('case1:', res1, nums1)
    print('case2:', res2, nums2)