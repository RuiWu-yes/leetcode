# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 39 组合总和
# @Content : 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates
#            中所有可以使数字和为 target 的组合。candidates 中的数字可以无限制重复被选取。
# @Explain : 1) 所有数字（包括 target）都是正整数。
#            2) 解集不能包含重复的组合。
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        # 回溯算法
        candidates.sort()
        res = []
        def backtrack(sums, start, track):
            if sums == target:
                res.append(track[:])
                return
            for i in range(start, len(candidates)):
                sums += candidates[i]
                if sums > target:  # 剪枝，路径track中元素和 > target，显然后面在添加元素不能满足返回条件
                    return
                track.append(candidates[i])
                backtrack(sums, i, track)  # 39_组合总和: i  40_组合总和I: i+1
                sums -= candidates[i]
                track.pop()
        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    # case1  res = [[7], [2, 2, 3]]
    candidates1 = [2, 3, 6, 7]
    target1 = 7

    # case2  res = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    candidates2 = [2, 3, 5]
    target2 = 8

    sol = Solution()
    res1 = sol.combinationSum(candidates1, target1)
    res2 = sol.combinationSum(candidates2, target2)
    print('case1:', res1)
    print('case2:', res2)