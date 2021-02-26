# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 78 子集
# @Content : 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# @Explain : 解集不能包含重复的子集。


class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(start, track):
            # 拷贝track并添加进res。如果不进行拷贝，由于track的地址不变，将会由track最后的状态(track在最后进行了出栈操作，故最后的状态为空)的值覆盖
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1
    nums = [1, 2, 3]

    s = Solution()
    res = s.subsets(nums)
    print(res)