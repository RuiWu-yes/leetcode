# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 332 重新安排行程
# @Content : 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
#            对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
#      提示 : 1) 如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"]
#               相比就更小，排序更靠前
#            2) 所有的机场都用三个大写字母表示（机场代码）。
#            3) 假定所有机票至少存在一种合理的行程。
#            4) 所有的机票必须都用一次 且 只能用一次。
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        # 回溯算法
        ticket_dict = defaultdict(list)
        for item in tickets:
            ticket_dict[item[0]].append(item[1])
        path = ['JFK']
        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:  # 结束条件
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
                path.append(cur_to)  # 做选择
                if backtrack(cur_to):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
                ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
            return False
        backtrack('JFK')
        return path


if __name__ == '__main__':
    # case1  res = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    # case2  res = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    # 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

    sol = Solution()
    res1 = sol.findItinerary(tickets1)
    res2 = sol.findItinerary(tickets2)
    print('case1:', res1)
    print('case2:', res2)