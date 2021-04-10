# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 152 乘积最大子数组
# @Content : 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
from typing import List


class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i]的定义：数组nums[:i]中最大的连续子数组乘积值
        # 状态转移：
        #    我们只要记录前i的最小值和最大值
        #    那么 dp[i] = max(nums[i] * ma, nums[i] * mi, nums[i]), 这里0 不需要单独考虑, 因为当相乘不管最大值和最小值,都会置0
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            # 举个例子： mi = -4, ma = -2, nums[i] = -1
            #    如果mi, ma不交换，则后面计算的mi = 4, ma = 2(不满足最大ma比最小mi大)
            #    如果mi, ma交换，则后面计算的mi = 2, ma = 4(满足最大ma比最小mi大)
            if nums[i] < 0:
                mi, ma = ma, mi
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            res = max(res, ma)
        return res

    def maxProduct2(self, nums: List[int]) -> int:
        # 根据符号的个数
        #    当负数个数为偶数时候，全部相乘一定最大
        #    当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
        #    当有 0 情况，重置就可以了
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


if __name__ == '__main__':
    # case1  res = 6
    # 解释: 子数组 [2,3] 有最大乘积 6。
    nums1 = [2, 3, -2, 4]

    # case2  res = 0
    # 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
    nums2 = [-2, 0, -1]

    sol = Solution()
    res1 = sol.maxProduct1(nums1), sol.maxProduct2(nums1)
    res2 = sol.maxProduct1(nums2), sol.maxProduct2(nums2)
    print('case1:', res1)
    print('case2:', res2)