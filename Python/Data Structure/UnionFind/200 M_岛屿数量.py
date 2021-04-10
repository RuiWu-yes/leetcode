# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 200 岛屿数量
# @Content : 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#            岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#            此外，你可以假设该网格的四条边均被水包围。
from typing import List


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS(染色法)
        # 思路：遍历所有节点，
        #      if node == ‘1': count += 1，然后将此node和附近的全部陆地('1')染成('0') --> BFS通过队列将node附近的全部(‘1’)节点添加到
        #                                  队列中，然后染色成('0')
        #      else: 不做任何处理
        if not grid or not grid[0]: return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()
        return sum([self.floodfill_BFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_BFS(self, x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        queue = [(x, y)]
        while queue:
            cur_x, cur_y = queue.pop(0)
            for i in range(4):
                new_x, new_y = cur_x + dx[i], cur_y + dy[i]
                if self._is_valid(new_x, new_y):
                    self.visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return 1

    def _is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS(染色法)
        # 思路：遍历所有节点，
        #      if node == ‘1': count += 1，然后将此node和附近的全部陆地('1')染成('0') --> DFS通过递归往node附近的节点扩散
        #      else: 不做任何处理
        if not grid or not grid[0]: return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()
        return sum([self.floodfill_DFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_DFS(self, x, y):
        # 四连通(左右上下)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodfill_DFS(x + dx[k], y + dy[k])
        return 1

    def _is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 并查集
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == '1':
                        uf.union(i * n + j, nr * n + nc)
        return uf.count

class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


if __name__ == '__main__':
    # case1  res = 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    # case2  res = 3
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    sol1, sol2, sol3 = Solution1(), Solution2(), Solution3()
    res1 = sol1.numIslands(grid1), sol2.numIslands(grid1), sol3.numIslands(grid1)
    res2 = sol1.numIslands(grid2), sol2.numIslands(grid2), sol3.numIslands(grid2)
    print('case1:', res1)
    print('case2:', res2)