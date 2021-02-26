# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 123 买卖股票的最佳时机 III
# @Content : 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#            设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# @Att     : 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, prices) -> int:
        # 动态规划
        #    原始的动态转移方程，没有可化简的地方
        #    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        if not prices: return 0
        n = len(prices)
        dp_i_1_0, dp_i_1_1 = 0, float('-inf')
        dp_i_2_0, dp_i_2_1 = 0, float('-inf')
        for i in range(n):
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            dp_i_1_1 = max(dp_i_1_1, -prices[i])
        return dp_i_2_0


if __name__ == '__main__':
    # # case1  res = 6
    # # 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    # #      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    # # case2  res = 4
    # # 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    # #      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    # #      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    # prices = [1, 2, 3, 4, 5]

    # # case3  res = 0
    # # 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
    # prices = [7, 6, 4, 3, 1]

    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)