# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 121 买卖股票的最佳时机
# @Content : 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#            设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# @Att     : 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 动态规划
        # 这个问题的「状态」有二个，第一个是天数，第二个是当前股票的持有状态（我们不妨用 1 表示持有，0 表示没有持有）
        # dp[i][0/1]的定义：在第 i 天，手上没有持有(0)或者持有(1)股票，所能获取的最大利润
        #    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 前一天没有持有股票，当天不进行任何操作/前一天持有股票，当天卖出股票
        #    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # 前一天持有股票，当天不进行任何操作/前一天没有持有股票，当天买入股票
        if not prices: return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0], dp[i][1] = 0, -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        # 动态规划：状态压缩
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0  # 显然手上没有持有股票才能获取最大利润

    def maxProfit3(self, prices: List[int]) -> int:
        # 贪心算法
        # 局部最优:收集每天的正利润
        # 全局最优:求得最大利润。
        # 思路：这道题目可能我们只会想,选一个低的买入,在选个高的卖,在选一个低的买入.....循环反复。
        #      如果想到其实最终利润是可以分解的,那么本题就很容易了!
        #      如果分解呢?
        #         假如第0天买入,第3天卖出,那么利润为:prices[3] - prices[0]。
        #         相当于(prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])。
        #         此时就是把利润分解为每天为单位的维度,而不是从0天到第3天整体去考虑!
        #         那么根据prices可以得到每天的利润序列:(prices[i] - prices[i - 1]).....(prices[1] - prices[0])。
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res


if __name__ == '__main__':
    # case1  res = 7
    # 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    #      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
    prices1 = [7, 1, 5, 3, 6, 4]

    # case2  res = 4
    # 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    #      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    #      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    prices2 = [1, 2, 3, 4, 5]

    # case2  res = 0
    # 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
    prices3 = [7, 6, 4, 3, 1]

    sol = Solution()
    res1 = sol.maxProfit1(prices1), sol.maxProfit2(prices1), sol.maxProfit3(prices1)
    res2 = sol.maxProfit1(prices2), sol.maxProfit2(prices2), sol.maxProfit3(prices2)
    res3 = sol.maxProfit1(prices3), sol.maxProfit2(prices3), sol.maxProfit3(prices3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)