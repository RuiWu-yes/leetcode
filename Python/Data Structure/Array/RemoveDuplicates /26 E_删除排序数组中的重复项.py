# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 26 删除排序数组中的重复项
# @Content : 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#            不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


class Solution:
    def removeDuplicates(self, nums) -> int:
        # 快慢指针
        if not nums: return 0
        slow = fast = 0
        while fast < len(nums):
            # 举例： [1, 1, 2] | [1, 2, 1]
            if nums[fast] != nums[slow]:
                slow += 1
                # 维护 nums[0..slow] 无重复
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


if __name__ == '__main__':
    # case1  res = 2 -> nums = [1, 2, 2]
    # 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
    # 你不需要考虑数组中超出新长度后面的元素。
    nums1 = [1, 1, 2]

    # case2  res = 5 -> nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    # 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
    # 你不需要考虑数组中超出新长度后面的元素。
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    sol = Solution()
    res1 = sol.removeDuplicates(nums1)
    res2 = sol.removeDuplicates(nums2)
    print('case1:', res1, nums1)
    print('case1:', res2, nums2)