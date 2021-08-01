# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 迪杰斯特拉算法求最短路径
# @Content : 实现迪杰斯特拉最短路径算法
import heapq


class Dijkstra:
    def dijkstra(self, graph, start):
        if not graph or not start:
            return

        distance = {key: float('inf') for key in graph.keys()}
        distance[start] = 0

        pqueue, visited = [], set()
        heapq.heappush(pqueue, (0, start))
        parent = {start: None}

        while pqueue:
            cur_distance, cur_node = heapq.heappop(pqueue)
            visited.add(cur_node)
            nodes = graph[cur_node]

            for node, dist in nodes.items():
                if node in visited:
                    continue
                if cur_distance + dist < distance[node]:
                    heapq.heappush(pqueue, (dist + cur_distance, node))
                    parent[node] = cur_node
                    distance[node] = cur_distance + dist
        return distance, parent

    def getpath(self, parent, end, start):
        stack = [end]
        while end != start:
            stack.append(parent[end])
            end = parent[end]
        return '->'.join(stack[::-1])


if __name__ == '__main__':
    # case1  res = {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}
    #      A
    #   5/ 2 \1
    #   B ——— C
    #  1|  /4 |8
    #   D ——— E
    #  6|  3
    #   F
    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6}
    }
    s = Dijkstra()
    res, parent = s.dijkstra(graph, "A")
    path = s.getpath(parent, 'F', 'A')
    print('case1 res: ', res)
    print('case1 parent: ', parent)
    print('case1 path: ', path)