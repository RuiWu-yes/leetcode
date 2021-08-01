# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 40 组合总和 II
# @Content : 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#            candidates 中的每个数字在每个组合中只能使用一次。
# @Explain : 1) 所有数字（包括目标数）都是正整数。
#            2) 解集不能包含重复的组合。


class Solution:
    def combinationSum2(self, candidates, target: int):
        # 回溯算法
        candidates.sort()
        res = []
        def backtrack(sums, start, track):
            if sums == target:
                res.append(track[:])
                return
            for i in range(start, len(candidates)):
                # 由于数组可能含有重复数字且返回的结果不能重复，因此同一层做选择的时候不能重复选择一样的数
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sums += candidates[i]
                if sums > target:  # 剪枝(路径track中元素和 > target，显然后面在添加元素不能满足返回条件)
                    return
                track.append(candidates[i])
                backtrack(sums, i+1, track)  # 39_组合总和: i  40_组合总和I: i+1
                sums -= candidates[i]
                track.pop()
        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    # case1  res = [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8

    # case2  res = [[1, 2, 2], [5]]
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5

    sol = Solution()
    res1 = sol.combinationSum2(candidates1, target1)
    res2 = sol.combinationSum2(candidates2, target2)
    print('case1:', res1)
    print('case2:', res2)