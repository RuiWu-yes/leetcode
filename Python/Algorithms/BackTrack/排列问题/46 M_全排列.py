# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 46 全排列
# @Content : 给定一个 没有重复 数字的序列，返回其所有可能的全排列。


class Solution:
    def permute1(self, nums):
        # DFS
        res = []
        def dfs(nums, track):
            if not nums:
                res.append(track)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], track+[nums[i]])
        dfs(nums, [])
        return res

    def permute2(self, nums):
        # 回溯算法1
        res = []
        def backtrack(track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] in track: continue
                track.append(nums[i])
                backtrack(track)
                track.pop()
        backtrack([])
        return res

    def permute3(self, nums):
        # 回溯算法2: 直接在nums中交换元素，效率更高
        def backtrack(position, end):
            if position == end:
                res.append(nums[:])
                return

            for index in range(position, end):
                nums[index], nums[position] = nums[position], nums[index]
                backtrack(position + 1, end)
                nums[index], nums[position] = nums[position], nums[index]
        res = []
        backtrack(0, len(nums))
        return res


if __name__ == '__main__':
    # case1  res = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    nums = [1, 2, 3]

    s = Solution()
    res1 = s.permute1(nums)
    res2 = s.permute2(nums)
    res3 = s.permute3(nums)
    print('DFS:', sorted(res1))
    print('回溯算法1:', sorted(res2))
    print('回溯算法2:', sorted(res3))