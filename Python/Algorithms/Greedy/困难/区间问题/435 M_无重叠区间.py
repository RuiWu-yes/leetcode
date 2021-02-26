# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 435 无重叠区间
# @Content : 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# @Att     : 1) 可以认为区间的终点总是大于它的起点。
#            2) 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # 贪心算法
        # 先求最多有几个区间不会重叠了，那么剩下的就是至少需要去除的区间
        if not intervals: return 0
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])  # 按 end 升序排序
        count = 1  # 至少有一个区间不相交
        x_end = intervals[0][1]  # 排序后，第一个区间就是 x
        for interval in intervals:
            start = interval[0]
            if start >= x_end:
                # 找到下一个选择的区间了
                count += 1
                x_end = interval[1]
        return n - count


if __name__ == '__main__':
    # case1  res = 1
    # 解释: 移除 [1,3] 后，剩下的区间没有重叠。
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]

    # case2  res = 2
    # 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
    intervals2 = [[1, 2], [1, 2], [1, 2]]

    # case3  res = 0
    # 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
    intervals3 = [[1, 2], [2, 3]]


    sol = Solution()
    res1 = sol.eraseOverlapIntervals(intervals1)
    res2 = sol.eraseOverlapIntervals(intervals2)
    res3 = sol.eraseOverlapIntervals(intervals3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)