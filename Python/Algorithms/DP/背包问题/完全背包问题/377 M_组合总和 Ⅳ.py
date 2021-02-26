# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 377 组合总和 Ⅳ
# @Content : 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
#            进阶：如果给定的数组中含有负数会怎么样？
#                 问题会产生什么变化？
#                 我们需要在题目中添加什么限制来允许负数的出现？


class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        # 动态规划
        # 完全背包-组合问题-排列问题
        # dp[i]: 对于给定的由正整数组成且不存在重复数字的数组，和为 i 的组合的个数。
        if not nums or target <= 0:
            return 0
        dp = [0 for _ in range(target + 1)]
        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这个值被其它状态参考，设置为 1 是合理的
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    # case1  res = 7
    # 所有可能的组合为：
    # (1, 1, 1, 1)
    # (1, 1, 2)
    # (1, 2, 1)
    # (1, 3)
    # (2, 1, 1)
    # (2, 2)
    # (3, 1)
    # 请注意，顺序不同的序列被视作不同的组合。
    nums = [1, 2, 3]
    target = 4

    sol = Solution()
    res = sol.combinationSum4(nums, target)
    print(res)