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
        if not grid or not grid[0]:  # [] or [[]]
            return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()  # 用集合去记录拜访过的元素
        return sum([self.floodfill_BFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_BFS(self, x, y):
        #     左  右  上  下
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
        # 判断是否可以染色
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:  # 超出边界
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):  # 若值为'0' 或者 已经被拜访过
            return False
        return True

class Solution1_1:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1  # 记录岛屿的个数
                    grid[r][c] = "0"  # 已经拜访过的直接归0
                    queue = [(r, c)]
                    while queue:
                        cur_x, cur_y = queue.pop(0)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_x, new_y = cur_x + dx, cur_y + dy
                            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "1":
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = "0"  # 已经拜访过的直接归0
        return num_islands


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS(染色法)
        # 思路：遍历所有节点，
        #      if node == ‘1': count += 1，然后将此node和附近的全部陆地('1')染成('0') --> DFS通过递归往node附近的节点扩散
        #      else: 不做任何处理
        if not grid or not grid[0]:  # [] or [[]]
            return 0
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
        for i in range(4):
            self.floodfill_DFS(x + dx[i], y + dy[i])
        return 1

    def _is_valid(self, x, y):
        # 判断是否可以染色
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True


class Solution2_1:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        if not grid or not grid[0]: return 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                    dfs(nr, nc)

        num_islands = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        return num_islands


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 并查集
        if not grid or not grid[0]:  # [] or [[]]
            return 0

        uf = UnionFind(grid)
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '0':
                    continue
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 左右上下
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':  # 只要当前位置的上下左右有'1'就合并
                        uf.union(r * col + c, nr * col + nc)
        return uf.count


class UnionFind:
    def __init__(self, grid):
        # 初始化
        row, col = len(grid), len(grid[0])
        self.count = 0  # 记录集合的个数
        self.parent = [-1] * (row * col)  # 初始化长度为grid的元素个数的数组, 记录集合的父节点
        self.rank = [0] * (row * col)  # 记录每个集合的秩(树的深度)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.parent[r * col + c] = r * col + c  # 初始化每个'1'元素为一个集合, 用元素在gird中的位置表示
                    self.count += 1  # 计数多少个集合(因为将每个'1'作为一个集合，那么有多少个'1'就有多少个集合)

    def find(self, i):
        # 查询
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]  # 返回查询的这颗树的根节点(即这个节点的父节点指向自己, 在数组中是其索引刚好等于其索引对应的值)

    def union(self, x, y):
        # 合并
        rootx = self.find(x)  # x所在树的根节点(索引)
        rooty = self.find(y)  # y所在树的根节点(索引)
        if rootx != rooty:  # 不相等说明x, y在不同的树上(即两个不同集合)
            # 按秩合并规则：
            #    把简单的树往复杂的树上合并，而不是相反。因为这样合并后，到根节点距离变长的节点个数比较少
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:  # 如果两个秩相等，那么rootx和rooty都可以作为合并后的根节点;但是此时合并后的树秩要+1
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
                # self.parent[rootx] = rooty
                # self.rank[rooty] += 1
            self.count -= 1  # 合并了，那总集合个数要少1个


if __name__ == '__main__':
    from copy import deepcopy
    # case1  res = 1
    grid1_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid1_2 = deepcopy(grid1_1)
    grid1_3 = deepcopy(grid1_1)

    # case2  res = 3
    grid2_1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid2_2 = deepcopy(grid2_1)
    grid2_3 = deepcopy(grid2_1)

    sol1, sol2, sol3 = Solution1_1(), Solution2_1(), Solution3()
    res1 = sol1.numIslands(grid1_1), sol2.numIslands(grid1_2), sol3.numIslands(grid1_3)
    res2 = sol1.numIslands(grid2_1), sol2.numIslands(grid2_2), sol3.numIslands(grid2_3)
    print('case1:', res1)
    print('case2:', res2)