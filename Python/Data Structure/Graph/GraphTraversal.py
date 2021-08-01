# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 无向图的DFS, BFS遍历
# @Content : 返回无向图的DFS, BFS遍历结果
class GraphTraversal:
    def dfs(self, graph, start):
        res = []
        stack = [start]
        visited = {start}
        while stack:
            vertex = stack.pop()
            res.append(vertex)
            nodes = graph[vertex]
            for w in nodes:
                if w not in visited:
                    stack.append(w)
                    visited.add(w)
        return res

    def bfs(self, graph, start):
        res = []
        queue = [start]
        visited = {start}
        while queue:
            vertex = queue.pop(0)
            res.append(vertex)
            nodes = graph[vertex]
            for w in nodes:
                if w not in visited:
                    queue.append(w)
                    visited.add(w)
        return res


if __name__ == '__main__':
    # case1  res_dfs = ['A', 'C', 'E', 'D', 'F', 'B']  res_bfs = ['A', 'B', 'C', 'D', 'E', 'F']
    #      A
    #    /   \
    #   B ——— C
    #   |  /  |
    #   D ——— E
    #   |
    #   F
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }
    GT = GraphTraversal()
    res_dfs = GT.dfs(graph, "A")
    res_bfs = GT.bfs(graph, "A")
    print('DFS: ', res_dfs)
    print('BFS: ', res_bfs)