# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 74 搜索二维矩阵
# @Content : 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#               1) 每行中的整数从左到右按升序排列。
#               2) 每行的第一个整数大于前一行的最后一个整数。
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分法
        m, n = len(matrix), len(matrix[0])
        if m == 0: return False
        left, right = 0, m * n - 1
        while left <= right:
            mid_idx = left + (right - left) // 2
            mid_element = matrix[mid_idx // n][mid_idx % n]
            if target == mid_element:
                return True
            elif target > mid_element:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        return False


if __name__ == '__main__':
    # case1  res = true
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3

    # case2  res = false
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13

    sol = Solution()
    res1 = sol.searchMatrix(matrix1, target1)
    res2 = sol.searchMatrix(matrix2, target2)
    print('case1:', res1)
    print('case2:', res2)