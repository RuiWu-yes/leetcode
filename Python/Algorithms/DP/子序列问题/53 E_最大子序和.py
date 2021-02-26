# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 53 最大子序和
# @Content : 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#       进阶: 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution:
    def maxSubArray1(self, nums) -> int:
        # 动态规划
        n = len(nums)
        if n == 0: return 0
        dp = [0 for _ in range(n)]
        # base case
        # 第一个元素前面没有子数组
        dp[0] = nums[0]
        # 状态转移方程
        for i in range(1, n):
            # 要么自成一派，要么和前面的子数组合并
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        # 得到 nums 的最大子数组
        return max(dp)

    def maxSubArray2(self, nums) -> int:
        # 动态规划：状态压缩
        n = len(nums)
        if n == 0: return 0
        # base case
        dp_0, dp_1 = nums[0], 0
        res = dp_0
        for i in range(1, n):
            dp_1 = max(nums[i], nums[i] + dp_0)
            dp_0 = dp_1
            res = max(res, dp_1)
        return res

    def maxSubArray3(self, nums) -> int:
        # 贪心算法
        # 局部最优:当前“连续和”为负数的时候立刻放弃,从下一个元素重新计算“连续和”,因为负数加上下一个元素 “连续和”只会越来越小。
        # 全局最优:选取最大“连续和”
        # 过程：遍历nums,从头开始用count累积,如果count一旦加上nums[i]变为负数,那么就
        #      应该从nums[i+1]开始从0累积count了,因为已经变为负数的count,只会拖累总和。
        res = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:  # 取区间累计的最大值(相当于不断确定最大子序终止位置
                res = count
            if count <= 0:  # 相当于重置最大子序起始位置,因为遇到负数一定是拉低总和
                count = 0
        return res


if __name__ == '__main__':
    # case1  res = 6
    # 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    sol = Solution()
    res1 = sol.maxSubArray1(nums)
    res2 = sol.maxSubArray2(nums)
    res3 = sol.maxSubArray3(nums)
    print('case1:', res1, res2, res3)