# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 121 买卖股票的最佳时机
# @Content : 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#            如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# @Att     : 你不能在买入股票前卖出股票。


class Solution:
    def maxProfit1(self, prices) -> int:
        # 动态规划1:DP table
        # 这个问题的「状态」有二个，第一个是天数，第二个是当前股票的持有状态（我们不妨用 1 表示持有，0 表示没有持有）
        # dp[i][0/1]的定义：在第 i 天，手上没有持有(0)或者持有(1)股票，所能获取的最大利润
        #    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 前一天没有持有股票，当天不进行任何操作/前一天持有股票，当天卖出股票
        #    dp[i][1] = max(dp[i-1][1], -prices[i])              # 前一天持有股票，当天不进行任何操作/前一天没有持有股票，当天买入股票
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # 状态转移
        for i in range(n):
            if i - 1 == -1:
                dp[i][0], dp[i][1] = 0, -prices[i]  # 状态初始化
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]  # 显然手上没有持有股票才能获取最大利润

    def maxProfit2(self, prices) -> int:
        # 动态规划2:不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1)
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0  # 显然手上没有持有股票才能获取最大利润


if __name__ == '__main__':
    # case1  res = 5
    # 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
    #      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
    prices1 = [7, 1, 5, 3, 6, 4]

    # # case2  res = 0
    # # 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
    prices2 = [7, 6, 4, 3, 1]

    sol = Solution()
    res1 = sol.maxProfit1(prices1), sol.maxProfit2(prices1)
    res2 = sol.maxProfit1(prices2), sol.maxProfit2(prices2)
    print('case1:', res1)
    print('case2:', res2)