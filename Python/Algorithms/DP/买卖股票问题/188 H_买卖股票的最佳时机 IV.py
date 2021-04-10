# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 188 买卖股票的最佳时机 IV
# @Content : 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#            设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# @Att     : 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, k, prices) -> int:
        # 动态规划
        # 传入的 k 值会非常大，dp 数组太大了。现在想想，交易次数 k 最多有多大呢？
        # 一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。
        #    原始的动态转移方程，没有可化简的地方
        #    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        if not prices: return 0
        n = len(prices)
        if k > n / 2:  # 相当于交易多少次不受限
            dp_i_0, dp_i_1 = 0, -prices[0]
            for i in range(1, n):
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
            return dp_i_0
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


if __name__ == '__main__':
    # case1  res = 2
    # 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    k1 = 2
    prices1 = [2, 4, 1]

    # case2  res = 7
    # 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
    #      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
    k2 = 2
    prices2 = [3, 2, 6, 5, 0, 3]

    sol = Solution()
    res1 = sol.maxProfit(k1, prices1)
    res2 = sol.maxProfit(k2, prices2)
    print('case1:', res1)
    print('case2:', res2)