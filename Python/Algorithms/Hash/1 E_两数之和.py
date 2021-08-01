# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1 两数之和
# @Content : 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#            你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#            你可以按任意顺序返回答案。


class Solution:
    def twoSum1(self, nums, target: int):
        # 暴力法: 时间复杂度 O(N^2)，空间复杂度 O(1)。
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return [-1, -1]

    def twoSum2(self, nums, target: int):
        # 两遍哈希
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dic and dic[val] != i:
                return [i, dic[val]]
        return [-1, -1]

    def twoSum3(self, nums, target: int):
        # 一遍哈希
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic.get(temp), i]
            else:
                dic[nums[i]] = i


if __name__ == '__main__':
    # case1  res = [0, 1]
    # 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]
    nums1 = [2, 7, 11, 15]
    target1 = 9

    # case2  res = [1, 2]
    nums2 = [3, 2, 4]
    target2 = 6

    # case3  res = [0, 1]
    nums3 = [3, 3]
    target3 = 6

    sol = Solution()
    res1 = sol.twoSum1(nums1, target1), sol.twoSum2(nums1, target1)
    res2 = sol.twoSum1(nums2, target2), sol.twoSum2(nums2, target2)
    res3 = sol.twoSum1(nums3, target3), sol.twoSum2(nums3, target3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)