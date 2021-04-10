# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 746 使用最小花费爬楼梯
# @Content : 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
#            每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
#            请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
from typing import List


class Solution1:
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        # 动态规划
        # 到达第i级台阶的阶梯顶部的最小花费，有两个选择：
        #    1) 先付出最小总花费minCost[i-1]到达第i级台阶（即第i-1级台阶的阶梯顶部），踏上第i级台阶需要再花费cost[i]，再迈一步到达第i级台阶
        #    的阶梯顶部，最小总花费为minCost[i-1] + cost[i])
        #    2) 先付出最小总花费minCost[i-2]到达第i-1级台阶（即第i-2级台阶的阶梯顶部），踏上第i-1级台阶需要再花费cost[i-1]，再迈两步跨过
        #    第i级台阶直接到达第i级台阶的阶梯顶部，最小总花费为minCost[i-2] + cost[i-1])
        # 则minCost[i]是上面这两个最小总花费中的最小值。
        #    minCost[i] = min(minCost[i-1] + cost[i], minCost[i-2] + cost[i-1])
        # 台阶的数组从0开始计数。可以用-1代表地面，并设cost[-1] = 0
        # 最小总花费的初始值为：
        #    第0级台阶： minCost[0] = min(cost[-1], cost[0]) = min(0, cost[0]) = 0
        #    第1级台阶： minCost[1] = min(cost[0], cost[1])
        n = len(cost)
        minCost = [0] * n
        minCost[1] = min(cost[0], cost[1])
        for i in range(2, n):
            minCost[i] = min(minCost[i - 1] + cost[i], minCost[i - 2] + cost[i - 1])
        return minCost[-1]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        # 动态规划(状态压缩)
        minCost0, minCost1 = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            minCost = min(minCost1 + cost[i], minCost0 + cost[i - 1])
            minCost0, minCost1 = minCost1, minCost
        return minCost


class Solution2:
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        # 动态规划
        # 到达第i级台阶的阶梯顶部的最小花费，有两个选择：
        #    最后踏上了第i级台阶，最小花费dp[i]，再迈一步到达第i级台阶楼层顶部；
        #    最后踏上了第i-1级台阶，最小花费dp[i-1]，再迈两步跨过第i级台阶直接到达第i级台阶的阶梯顶部。
        # 所以到达第i级台阶的阶梯顶部的最小花费为minCost[i] = min(dp[i], dp[i-1])。
        # 即为了求出到达第i级台阶的阶梯顶部的最小花费，我们先算出踏上第i级台阶的最小花费，用dp[i]表示，
        # 再通过min(dp[i], dp[i-1])来求出到达第i级台阶的阶梯顶部的最小花费。
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[-2], dp[-1])

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        # 动态规划(状态压缩)
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[-2], cost[-1])


if __name__ == '__main__':
    # case1  res = 15
    # 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
    cost1 = [10, 15, 20]

    # case2  res = 6
    # 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    sol1 = Solution1()
    res1_1 = sol1.minCostClimbingStairs1(cost1), sol1.minCostClimbingStairs1(cost1)
    res1_2 = sol1.minCostClimbingStairs1(cost2), sol1.minCostClimbingStairs2(cost2)

    sol2 = Solution2()
    res2_1 = sol2.minCostClimbingStairs1(cost1), sol2.minCostClimbingStairs1(cost1)
    res2_2 = sol2.minCostClimbingStairs1(cost2), sol2.minCostClimbingStairs2(cost2)
    print('case1:', res1_1, res2_1)
    print('case2:', res1_2, res2_2)