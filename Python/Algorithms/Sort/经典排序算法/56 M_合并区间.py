# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 56 合并区间
# @Content : 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
#            请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 贪心算法
        # 那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，
        # 整体最优：合并所有重叠的区间。
        res = []
        if not intervals: return res
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:  # 合并区间
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    # case1  res = [[1,6],[8,10],[15,18]]
    # 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]

    # case2  res = [[1,5]]
    # 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
    intervals2 = [[1, 4], [4, 5]]

    sol = Solution()
    res1 = sol.merge(intervals1)
    res2 = sol.merge(intervals2)
    print('case1:', res1)
    print('case2:', res2)