# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 135 分发糖果
# @Content : 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#            你需要按照以下要求，帮助老师给这些孩子分发糖果：
#            每个孩子至少分配到 1 个糖果。
#            评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
#            那么这样下来，老师至少需要准备多少颗糖果呢？
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 贪心算法
        # 局部最优：只要右边评分比左边大，右边的孩子就多一个糖果
        # 全局最优：相邻的孩子中，评分高的右孩子获得比左边孩子更多的糖果
        candyVec = [1] * len(ratings)
        # 从前往后
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1
        # 从后向前
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candyVec[i] = max(candyVec[i], candyVec[i + 1] + 1)
        # 统计结果
        return sum(candyVec)


if __name__ == '__main__':
    # case1  res = 5
    # 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
    ratings1 = [1, 0, 2]

    # case2  res = 4
    # 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
    #      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
    ratings2 = [1, 2, 2]

    sol = Solution()
    res1 = sol.candy(ratings1)
    res2 = sol.candy(ratings2)
    print('case1:', res1)
    print('case2:', res2)