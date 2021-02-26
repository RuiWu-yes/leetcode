# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 198 打家劫舍
# @Content : 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果
#            两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#            给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


class Solution:
    def rob1(self, nums) -> int:
        # 动态规划：带备忘录的递归
        #    dp[nums, 0] = max(dp(nums, start + 1), nums[start] + dp(nums, start + 2))
        #                      不偷，进入下一个房子     偷，下个房子不能偷，只能到下下个房子
        if not nums: return 0
        memo = {}
        def dp(nums, start):
            if start >= len(nums):
                return 0
            if start in memo:  # 避免重复计算
                return memo[start]
            res = max(dp(nums, start + 1), nums[start] + dp(nums, start + 2))
            memo[start] = res
            return res
        return dp(nums, 0)

    def rob2(self, nums) -> int:
        # 动态规划：dp table
        if not nums: return 0
        n = len(nums)
        dp = [0 for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        return dp[0]

    def rob3(self, nums) -> int:
        # 动态规划：对dp table进行优化，空间复杂度降低为O(1)
        # 状态转移方程：dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        # 从状态转移方程可以看出当前状态dp[i]与dp[i+1]和dp[i+2]有关，所以可以用两个变量记录dp[i+1]和dp[i+2]
        if not nums: return 0
        n = len(nums)
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(n-1, -1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i


if __name__ == '__main__':
    # case1  res = 4
    # 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    #      偷窃到的最高金额 = 1 + 3 = 4 。
    nums = [1, 2, 3, 1]

    # # case2  res = 12
    # # 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    # #      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    # nums = [2, 7, 9, 3, 1]

    sol = Solution()
    res1 = sol.rob1(nums)
    res2 = sol.rob2(nums)
    res3 = sol.rob3(nums)
    print(res1, res2, res3)