# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 130 被围绕的区域
# @Content : 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#            找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
from typing import List


# 从边界出发吧，先把边界上和 O 连通点找到, 把这些变成 B,然后遍历整个 board 把 O 变成 X, 把 B 变成 O
# 所以这样就有 2 种方法
#    思路一: DFS
#    思路二: BFS
class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS
        if not board or not board[0]:
            return
        row, col = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + x, j + y
                # 为什么从1开始，因为题目要求边界上的'O'不算被'X'围绕
                if 1 <= ni < row and 1 <= nj < col and board[ni][nj] == "O":
                    dfs(ni, nj)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        # BFS
        if not board or not board[0]:
            return
        row, col = len(board), len(board[0])

        def bfs(i, j):
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0)
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.append((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

class Solution3:
    def solve(self, board: List[List[str]]) -> None:
        # UnionFind
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(y)] = find(x)

        if not board or not board[0]:
            return
        row, col = len(board), len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:  # 边界
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


if __name__ == '__main__':
    from copy import deepcopy

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
    board2 = deepcopy(board1)
    board3 = deepcopy(board1)

    # DFS
    sol1 = Solution1()
    sol1.solve(board1)
    # BFS
    sol2 = Solution2()
    sol2.solve(board2)
    # UnionFind
    sol3 = Solution3()
    sol3.solve(board3)

    print('DFS:', board1)
    print('BFS:', board2)
    print('UnionFind:', board3)