# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 90 子集 II
# @Content : 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# @Explain : 解集不能包含重复的子集。


class Solution:
    def subsetsWithDup(self, nums):
        # 回溯算法
        nums.sort()
        res = []
        def backtrack(start, track):
            res.append(track[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1  res = [[], [1], [1,2], [1,2,2], [2], [2,2]]
    nums1 = [1, 2, 2]

    # case2  res = [[], [1], [1,4], [1,4,4], [1,4,4,4], [1,4,4,4,4], [4], [4,4], [4,4,4], [4,4,4,4]]
    nums2 = [4, 4, 4, 1, 4]

    sol = Solution()
    res1 = sol.subsetsWithDup(nums1)
    res2 = sol.subsetsWithDup(nums2)
    print('case1:', res1)
    print('case2:', res2)