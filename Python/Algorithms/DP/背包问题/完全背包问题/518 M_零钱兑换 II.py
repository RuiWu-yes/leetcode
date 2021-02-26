# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 518 零钱兑换 II
# @Content : 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。


class Solution:
    def change1(self, amount: int, coins) -> int:
        # 动态规划
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        # base case
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]

    def change2(self, amount: int, coins) -> int:
        # 动态规划: 状态压缩
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        # base case
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]


if __name__ == '__main__':
    # case1  res = 4
    # 解释: 有四种方式可以凑成总金额:
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1
    amount1 = 5
    coins1 = [1, 2, 5]

    # case2  res = 0
    # 解释: 只用面额2的硬币不能凑成总金额3。
    amount2 = 3
    coins2 = [2]

    # case3  res = 1
    amount3 = 10
    coins3 = [10]

    sol = Solution()
    res1_1 = sol.change1(amount1, coins1)
    res1_2 = sol.change1(amount2, coins2)
    res1_3 = sol.change1(amount3, coins3)
    res2_1 = sol.change2(amount1, coins1)
    res2_2 = sol.change2(amount2, coins2)
    res2_3 = sol.change2(amount3, coins3)
    print('case1:', res1_1, res2_1)
    print('case2:', res1_2, res2_2)
    print('case3:', res1_3, res2_3)
