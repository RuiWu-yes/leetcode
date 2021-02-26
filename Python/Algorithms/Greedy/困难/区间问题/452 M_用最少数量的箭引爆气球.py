# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 452 用最少数量的箭引爆气球
# @Content : 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，
#            因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
#
#            一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
#            xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球
#            全部被引爆，所需的弓箭的最小数量。
#
#            给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。


class Solution:
    def findMinArrowShots(self, points) -> int:
        # 贪心算法
        if not points: return 0
        points.sort(key=lambda x: x[1])  # 按 end 升序排序
        count = 1  # 至少有一个区间不相交
        x_end = points[0][1]  # 排序后，第一个区间就是 x
        for interval in points:
            start = interval[0]
            if start > x_end:
                # 找到下一个选择的区间了
                count += 1
                x_end = interval[1]
        return count


if __name__ == '__main__':
    # case1  res = 2
    # 解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]

    # case2  res = 4
    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]

    # case3  res = 2
    points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]

    # case4  res = 1
    points4 = [[1, 2]]

    # case5  res = 1
    points5 = [[2, 3], [2, 3]]

    sol = Solution()
    res1 = sol.findMinArrowShots(points1)
    res2 = sol.findMinArrowShots(points2)
    res3 = sol.findMinArrowShots(points3)
    res4 = sol.findMinArrowShots(points4)
    res5 = sol.findMinArrowShots(points5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)