# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 52 N皇后 II
# @Content : n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#            给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#      提示 ：1) 1 <= n <= 9
#            2) 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。


class Solution:
    def totalNQueens(self, n: int) -> int or []:
        if n < 1: return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        # recursion terminator
        if row >= n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位

        while bits:
            p = bits & -bits  # 取到最低位的1
            bits = bits & (bits - 1)  # 表示在p位置上放入皇后
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            # 不需要revert  cols, pie, na 的状态


if __name__ == '__main__':
    # case1  res = 2
    # 解释：如上图所示，4 皇后问题存在两个不同的解法。
    n1 = 4

    # case2  res = 1
    n2 = 1

    sol = Solution()
    res1 = sol.totalNQueens(n1)
    res2 = sol.totalNQueens(n2)
    print('case1:', res1)
    print('case2:', res2)