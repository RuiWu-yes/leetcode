# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 329 矩阵中的最长递增路径
# @Content : 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
#            对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
from typing import List
from functools import lru_cache
import collections


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 方法一：记忆化深度优先搜索
        if not matrix: return 0

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = row + dx, column + dy
                if 0 <= nx < rows and 0 <= ny < columns and matrix[nx][ny] > matrix[row][column]:
                    best = max(best, dfs(nx, ny) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        # 方法二：拓扑排序
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < columns and matrix[nx][ny] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and matrix[nx][ny] < matrix[x][y]:
                        outdegrees[nx][ny] -= 1
                        if outdegrees[nx][ny] == 0:
                            queue.append((nx, ny))

        return ans


if __name__ == '__main__':
    # case1  res = 4
    # 解释：最长递增路径为 [1, 2, 6, 9]
    matrix1 = [[9, 9, 4],
               [6, 6, 8],
               [2, 1, 1]]

    # case2  res = 4
    # 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动
    matrix2 = [[3, 4, 5],
               [3, 2, 6],
               [2, 2, 1]]

    # case3  res = 1
    matrix3 = [[1]]

    sol = Solution()
    res1 = sol.longestIncreasingPath(matrix1), sol.longestIncreasingPath2(matrix1)
    res2 = sol.longestIncreasingPath(matrix2), sol.longestIncreasingPath2(matrix2)
    res3 = sol.longestIncreasingPath(matrix3), sol.longestIncreasingPath2(matrix3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)