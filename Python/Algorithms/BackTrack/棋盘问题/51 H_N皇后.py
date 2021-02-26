# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 51 N皇后
# @Content : n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#            给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。


class Solution:
    def solveNQueens1(self, n):
        # DFS
        res = []
        # queens:皇后在每一行的位置； xy_dif:一个对角线； xy_sum:另一个对角线
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]

    def solveNQueens2(self, n):
        # 回溯算法
        pass


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens1(4)
    # res = s.solveNQueens2(4)
    for i in range(len(res)):
        print('解法:', i+1)
        for j in range(len(res[i])):
            print(res[i][j])