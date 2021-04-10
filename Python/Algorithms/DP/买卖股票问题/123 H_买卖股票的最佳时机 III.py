# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 123 买卖股票的最佳时机 III
# @Content : 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#            设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# @Att     : 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit1(self, prices) -> int:
        # 动态规划
        # 这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，第三个是当前的持有状态（我们不妨用 1 表示持有，0 表示没有持有）
        # dp[i][1/2][0/1]的定义：在第 i 天，第k次交易(k最多为2)，手上没有持有(0)或者持有(1)股票，所能获取的最大利润
        #    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        k, n = 2, len(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]

    def maxProfit2(self, prices) -> int:
        # 动态规划：状态压缩
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
    prices1 = [3, 3, 5, 0, 0, 3, 1, 4]

    # case2  res = 4
    # 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    #      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    #      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    prices2 = [1, 2, 3, 4, 5]

    # case3  res = 0
    # 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
    prices3 = [7, 6, 4, 3, 1]

    sol = Solution()
    res1 = sol.maxProfit1(prices1), sol.maxProfit2(prices1)
    res2 = sol.maxProfit1(prices2), sol.maxProfit2(prices2)
    res3 = sol.maxProfit1(prices3), sol.maxProfit2(prices3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)