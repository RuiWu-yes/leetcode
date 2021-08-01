# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 221 最大正方形
# @Content : 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划
        # dp(i,j)的定义： 以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值
        # 如果我们能计算出所有 dp(i,j) 的值，那么其中的最大值即为矩阵中只包含 1 的正方形的边长最大值，其平方即为最大正方形的面积。
        # 那么如何计算 dp 中的每个元素值呢？对于每个位置 (i,j)，检查在矩阵中该位置的值：
        #    1) 如果该位置的值是 0，则 dp(i,j)=0，因为当前位置不可能在由 1 组成的正方形中；
        #    2) 如果该位置的值是 1，则 dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。
        #       具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1
        #    状态转移方程如下：
        #       dp(i, j) = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


if __name__ == '__main__':
    # case1  res = 4
    matrix1 = [["1", "0", "1", "0", "0"],
               ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"],
               ["1", "0", "0", "1", "0"]]

    # case2  res = 1
    matrix2 = [["0", "1"],
               ["1", "0"]]

    # case3  res = 0
    matrix3 = [["0"]]

    sol = Solution()
    res1 = sol.maximalSquare(matrix1)
    res2 = sol.maximalSquare(matrix2)
    res3 = sol.maximalSquare(matrix3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)