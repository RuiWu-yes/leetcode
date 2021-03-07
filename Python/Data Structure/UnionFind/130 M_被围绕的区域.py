# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 130 被围绕的区域
# @Content : 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#            找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass


if __name__ == '__main__':
    # case1
    # 输出：
    # [['X', 'X', 'X', 'X'],
    #  ['X', 'X', 'X', 'X'],
    #  ['X', 'X', 'X', 'X'],
    #  ['X', 'O', 'X', 'X']]
    board1 = [['X', 'X', 'X', 'X'],
              ['X', 'O', 'O', 'X'],
              ['X', 'X', 'O', 'X'],
              ['X', 'O', 'X', 'X']]

    sol = Solution()
    res1 = sol.solve(board1)
    print('case1:', res1)