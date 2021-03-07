# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 22 括号生成
# @Content : 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。


class Solution:
    def generateParenthesis1(self, n: int):
        # 深度优先搜索
        res = []
        def dfs(left, right, n, s):
            if left == n and right == n:
                return res.append(s)

            if left < n:
                dfs(left + 1, right, n, s + "(")
            if left > right:
                dfs(left, right + 1, n, s + ")")
        dfs(0, 0, n, "")
        return res

    def generateParenthesis2(self, n: int):
        # 回溯算法
        if n == 0: return
        res, track = [], []  # res: 记录所有合法的括号组合  track: 回溯过程中的路径
        # 可用的左括号数量为 left 个，可用的右括号数量为 rgiht 个
        def backtrack(left, right, track, res):
            # 若左括号剩下的多，说明不合法
            if right < left: return
            # 数量小于0肯定是不合法的
            if left < 0 or right < 0: return
            # 当所有括号都恰好用完时，得到一个合法的括号组合
            if left == 0 and right == 0:
                res.append(''.join(track[:]))
                return

            # 尝试放一个左括号
            track.append('(')  # 选择
            backtrack(left - 1, right, track, res)
            track.pop()  # 撤销选择

            # 尝试放一个右括号
            track.append(')')  # 选择
            backtrack(left, right - 1, track, res)
            track.pop()  # 撤销选择
        # 可用的左括号和右括号数量初始化为n
        backtrack(n, n, track, res)
        return res


if __name__ == '__main__':
    # case1
    # 输出：[
    #        "((()))",
    #        "(()())",
    #        "(())()",
    #        "()(())",
    #        "()()()"
    #      ]
    n = 3

    sol = Solution()
    res1 = sol.generateParenthesis1(n)
    res2 = sol.generateParenthesis2(n)
    print('深度优先方法:', res1)
    print('   回溯算法:', res2)