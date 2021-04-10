# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 85 最大矩形
# @Content : 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 6
    matrix1 = [["1", "0", "1", "0", "0"],
               ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"],
               ["1", "0", "0", "1", "0"]]

    # case2  res = 0
    matrix2 = []

    # case3  res = 0
    matrix3 = [["0"]]

    # case4  res = 1
    matrix4 = [["1"]]

    # case5  res = 0
    matrix5 = [["0", "0"]]

    sol = Solution()
    res1 = sol.maximalRectangle(matrix1)
    res2 = sol.maximalRectangle(matrix2)
    res3 = sol.maximalRectangle(matrix3)
    res4 = sol.maximalRectangle(matrix4)
    res5 = sol.maximalRectangle(matrix5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)