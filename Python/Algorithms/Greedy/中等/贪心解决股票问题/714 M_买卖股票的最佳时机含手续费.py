# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 714 买卖股票的最佳时机含手续费
# @Content : 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#            你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#            返回获得利润的最大值。
# @Att     : 这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。


class Solution:
    def maxProfit1(self, prices, fee: int) -> int:
        # 贪心算法
        # 如果使用贪心策略，就是最低值买，最高值（如果算上手续费还盈利）就卖。
        # 此时无非就是要找到两个点，买入日期和卖出日期。
        #     买入日期：其实很好想，遇到更低点就记录一下。
        #     卖出日期：这个就不好算了，但也没有必要算出准确的卖出日期，只要当前价格大于（最低价格+手续费），就可以收获利润，
        #             至于准确的卖出日期，就是连续收获利润区间里的最后一天（并不需要计算是具体哪一天）。
        #
        # 所以我们在做收获利润操作的时候其实有三种情况：
        #     情况一：收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），所以后面要继续收获利润。
        #     情况二：前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。
        #     情况三：不作操作，保持原有状态（买入，卖出，不买不卖）
        res = 0
        minPrice = prices[0]  # 记录最低价格
        for i in range(1, len(prices)):
            # 情况二：相当于买入
            if prices[i] < minPrice:
                minPrice = prices[i]
            # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
            if prices[i] >= minPrice and prices[i] <= minPrice + fee:
                continue
            # 计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
            if prices[i] > minPrice + fee:
                res += prices[i] - minPrice - fee
                minPrice = prices[i] - fee  # 情况一，这一步很关键
        return res

    def maxProfit2(self, prices, fee: int) -> int:
        # 动态规划
        #    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        #    解释：相当于买入股票的价格升高了。
        #         在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
        if not prices: return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)
        return dp_i_0


if __name__ == '__main__':
    # case1  res = 8
    # 解释: 能够达到的最大利润:
    # 在此处买入prices[0] = 1
    # 在此处卖出 prices[3] = 8
    # 在此处买入 prices[4] = 4
    # 在此处卖出 prices[5] = 9
    # 总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2

    sol = Solution()
    res1, res2 = sol.maxProfit1(prices, fee), sol.maxProfit2(prices, fee)
    print('case1:', res1, res2)