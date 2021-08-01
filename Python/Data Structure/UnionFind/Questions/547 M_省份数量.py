# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 547 省份数量
# @Content : 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#            省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#            给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
#            而 isConnected[i][j] = 0 表示二者不直接相连。
#            返回矩阵中 省份 的数量。
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        counts = 0

        for i in range(provinces):
            if i not in visited:
                queue = [i]
                while queue:
                    j = queue.pop(0)
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            queue.append(k)
                counts += 1

        return counts


if __name__ == '__main__':
    # case1  res = 2
    isConnected1 = [[1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]]

    # case2  res = 3
    isConnected2 = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]

    # case3  res = 1
    isConnected3 = [[1, 0, 0, 1],
                    [0, 1, 1, 0],
                    [0, 1, 1, 1],
                    [1, 0, 1, 1]]

    sol = Solution()
    res1 = sol.findCircleNum(isConnected1)
    res2 = sol.findCircleNum(isConnected2)
    print('case1:', res1)
    print('case2:', res2)