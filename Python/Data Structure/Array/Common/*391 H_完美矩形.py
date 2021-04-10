# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 391 完美矩形
# @Content : 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
#            每个矩形用左下角的点和右上角的点的坐标来表示。例如，一个单位正方形可以表示为 [1,1,2,2]。
#            ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        pass


if __name__ == '__main__':
    # case1  res = true
    # 5个矩形一起可以精确地覆盖一个矩形区域。
    rectangles1 = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]

    # case2  res = false
    # 两个矩形之间有间隔，无法覆盖成一个矩形。
    rectangles2 = [
        [1, 1, 2, 3],
        [1, 3, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 4, 4]
    ]

    # case3  res = false
    # 图形顶端留有间隔，无法覆盖成一个矩形。
    rectangles3 = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [3, 2, 4, 4]
    ]

    # case4  res = false
    # 因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
    rectangles4 = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [2, 2, 4, 4]
    ]

    sol = Solution()
    res1 = sol.isRectangleCover(rectangles1)
    res2 = sol.isRectangleCover(rectangles2)
    res3 = sol.isRectangleCover(rectangles3)
    res4 = sol.isRectangleCover(rectangles4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)