# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 491 递增子序列
# @Content : 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。


class Solution:
    def findSubsequences(self, nums):
        # 回溯算法
        res = []
        def backtrack(start, track):
            if len(track) >= 2:
                res.append(track[:])
            map = {}
            for i in range(start, len(nums)):
                if map.get(nums[i], 0):  # 由于数组可能含有重复数字且返回的结果不能重复，因此同一层做选择的时候不能重复选择一样的数
                    continue
                if not track or (track and nums[i] >= track[-1]):  # or(前半部分: 路径为空; 后半部分: 判断递增子序列的条件)
                    track.append(nums[i])
                    map[nums[i]] = 1  # 1代表有, 0代表没有
                    backtrack(i+1, track)
                    track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1  res = [[4,6], [4,7], [4,6,7], [4,6,7,7], [6,7], [6,7,7], [7,7], [4,7,7]]
    nums = [4, 6, 7, 7]

    sol = Solution()
    res = sol.findSubsequences(nums)
    print('case1:', res)