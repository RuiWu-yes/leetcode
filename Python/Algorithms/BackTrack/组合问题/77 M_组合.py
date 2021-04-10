# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 77 组合
# @Content : 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


class Solution:
    def combine(self, n, k):
        # 回溯算法
        res = []
        if k <= 0 or n <= 0:
            return res
        def backtrack(n, k, start, track):
            if k == len(track):
                res.append(track[:])
                return
            for i in range(start, n+1):
                track.append(i)
                backtrack(n, k, i+1, track)
                track.pop()
        backtrack(n, k, 1, [])
        return res


if __name__ == '__main__':
    # case1
    n, k = 4, 2

    s = Solution()
    res = s.combine(n, k)
    print(res)