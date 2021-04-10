# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 494 目标和
# @Content : 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 - 。
#            对于数组中的任意一个整数，你都可以从 + 或 - 中选择一个符号添加在前面。
#            返回可以使最终数组和为目标数 S 的所有添加符号的方法数。


class Solution:
    def findTargetSumWays1(self, nums, S: int) -> int:
        # 回溯算法: 暴力解法，时间复杂度为 O(2^N)，LeetCode会超出时间限制
        if not nums: return 0
        result = 0
        def backtrack(nums, i, rest):
            nonlocal result
            # base case
            if i == len(nums):
                if rest == 0:
                    # 说明恰好凑出 target
                    result += 1
                return
            # 给 nums[i] 选择 - 号
            rest += nums[i]
            # 穷举 nums[i + 1]
            backtrack(nums, i+1, rest)
            # 撤销选择
            rest -= nums[i]

            # 给 nums[i] 选择 + 号
            rest -= nums[i]
            # 穷举 nums[i + 1]
            backtrack(nums, i + 1, rest)
            # 撤销选择
            rest += nums[i]
        backtrack(nums, 0, S)
        return result

    def findTargetSumWays2(self, nums, S: int) -> int:
        # 动态规划:带备忘录的递归解法
        if not nums: return 0
        memo = {}
        def dp(nums, i, rest):
            # base case
            if i == len(nums):
                if rest == 0: return 1
                return 0
            # 避免重复计算
            if (i, rest) in memo: return memo[(i, rest)]
            # 还是穷举
            result = dp(nums, i + 1, rest - nums[i]) + dp(nums, i + 1, rest + nums[i])
            # 记入备忘录
            memo[(i, rest)] = result
            return result
        return dp(nums, 0, S)


if __name__ == '__main__':
    # case1  res = 5
    # 解释：
    # -1+1+1+1+1 = 3
    # +1-1+1+1+1 = 3
    # +1+1-1+1+1 = 3
    # +1+1+1-1+1 = 3
    # +1+1+1+1-1 = 3
    # 一共有5种方法让最终目标和为3。
    nums = [1, 1, 1, 1, 1]
    S = 3

    sol = Solution()
    res1 = sol.findTargetSumWays1(nums, S)
    res2 = sol.findTargetSumWays2(nums, S)
    print('case1:', res1, res2)