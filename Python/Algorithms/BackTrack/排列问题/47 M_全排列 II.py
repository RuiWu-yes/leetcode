# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 47 全排列 II
# @Content : 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。


class Solution:
    def permuteUnique(self, nums):
        # 回溯算法
        nums.sort()
        res = []
        def backtrack(visited, track):
            # visited = [0] * len(nums): 利用数组的索引记录元素是否访问过
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                # 1) 由于每次选择都是遍历整个数组，因此选择过的数要忽略
                # 2) 由于数组可能含有重复数字且返回的结果不能重复，因此同一层做选择的时候不能重复选择一样的数
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                track.append(nums[i])
                visited[i] = 1
                backtrack(visited, track)
                visited[i] = 0
                track.pop()
        backtrack([0]*len(nums), [])
        return res


if __name__ == '__main__':
    # case1  res = [[1,1,2], [1,2,1], [2,1,1]]
    nums1 = [1, 1, 2]

    # case2  res = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    nums2 = [1, 2, 3]

    sol = Solution()
    res1 = sol.permuteUnique(nums1)
    res2 = sol.permuteUnique(nums2)
    print('case1:', res1)
    print('case2:', res2)