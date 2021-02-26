# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 309 最佳买卖股票时机含冷冻期
# @Content : 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
#            设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#               你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#               卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


class Solution:
    def maxProfit(self, prices) -> int:
        # 动态规划
        #    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #    dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        #    解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        dp_pre_0 = 0  # 代表dp[i-2][0]
        for i in range(n):
            temp = dp_i_0  # 使用临时temp存下次的dp[i-2][0]
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    # case1  res = 3
    # 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    prices = [1, 2, 3, 0, 2]

    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)