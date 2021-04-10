# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 134 加油站
# @Content : 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#            你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。
#            你从其中的一个加油站出发，开始时油箱为空。
#            如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
# @Explain : 1) 如果题目有解，该答案即为唯一答案。
#            2) 输入数组均为非空数组，且长度相同。
#            3) 输入数组中的元素均为非负数。
from typing import List


class Solution:
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        # 贪心算法
        # 直接从全局进行贪心选择，情况如下：
        # 情况一：如果gas的总和小于cost总和，那么无论从哪里出发，一定是跑不了一圈的
        # 情况二：rest[i] = gas[i] - cost[i]为一天剩下的油，i从0开始计算累加到最后一站，如果累加没有出现负数，
        #       说明从0出发，油就没有断过，那么0就是起点。
        # 情况三：如果累加的最小值是负数，汽车就要从非0节点出发，从后向前，看哪个节点能这个负数填平，能把这个负数填平的节点就是出发节点。
        curSum = 0
        min = float('inf')  # 从起点出发，油箱里的油量最小值
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            curSum += rest
            if curSum < min: min = curSum
        if curSum < 0: return -1  # 情况一
        if min >= 0: return 0  # 情况二
        # 情况三
        for i in range(len(gas)-1, -1, -1):
            rest = gas[i] - cost[i]
            min += rest
            if min >= 0:
                return i
        return -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        # 贪心算法
        # 局部最优：当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1，因为从j开始一定不行。
        # 全局最优：找到可以跑一圈的起始位置。
        curSum = totalSum = 0
        start = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:     # 当前累加rest[i]和 curSum一旦小于0
                start = i + 1  # 起始位置更新为i+1
                curSum = 0     # curSum从0开始
        if totalSum < 0: return -1  # 说明怎么走都不可能跑一圈了
        return start


if __name__ == '__main__':
    # case1  res = 3
    # 解释:
    # 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
    # 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
    # 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
    # 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
    # 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
    # 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
    # 因此，3 可为起始索引。
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]

    # case2  res = -1
    # 解释:
    # 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
    # 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
    # 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
    # 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
    # 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
    # 因此，无论怎样，你都不可能绕环路行驶一周。
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]

    sol = Solution()
    res1 = sol.canCompleteCircuit1(gas1, cost1), sol.canCompleteCircuit2(gas1, cost1)
    res2 = sol.canCompleteCircuit1(gas2, cost2), sol.canCompleteCircuit2(gas2, cost2)
    print('case1:', res1)
    print('case2:', res2)