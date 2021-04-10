# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 84 柱状图中最大的矩形
# @Content : 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#            求在该柱状图中，能够勾勒出来的矩形的最大面积。
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 栈(先入后出)
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


if __name__ == '__main__':
    # case1  res = 10
    heights1 = [2, 1, 5, 6, 2, 3]

    sol = Solution()
    res1 = sol.largestRectangleArea(heights1)
    print('case1:', res1)