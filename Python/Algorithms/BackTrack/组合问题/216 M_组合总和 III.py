# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 216 组合总和 III
# @Content : 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# @Explain : 1) 所有数字都是正整数。
#            2) 解集不能包含重复的组合。


class Solution:
    def combinationSum3(self, k: int, n: int):
        # 回溯算法
        res = []
        def backtrack(start, track):
            if len(track) == k and sum(track) == n:
                res.append(track[:])
                return
            # 剪枝
            if len(track) > k or sum(track) > n:
                return
            for i in range(start, 10):
                track.append(i)
                backtrack(i+1, track)
                track.pop()
        backtrack(1, [])
        return res


if __name__ == '__main__':
    # case1  res = [[1, 2, 4]]
    k1 = 3
    n1 = 7

    # case2  res = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    k2 = 3
    n2 = 9

    sol = Solution()
    res1 = sol.combinationSum3(k1, n1)
    res2 = sol.combinationSum3(k2, n2)
    print('case1:', res1)
    print('case2:', res2)