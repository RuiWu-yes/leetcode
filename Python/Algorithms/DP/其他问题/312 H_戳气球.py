# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 312 戳气球
# @Content : 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。现在要求你戳破所有的气球。
#            戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。这里的 i - 1 和 i + 1 代表和
#            i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。求所能获得硬币的最大数量。


class Solution:
    def maxCoins1(self, nums) -> int:
        # 回溯算法
        # 时间复杂度是阶乘级别，非常高
        # Leetcode提交答案会超过时间限制
        res = 0
        def backtrack(nums, score):
            nonlocal res
            if not nums:
                res = max(res, score)
                return
            for i in range(len(nums)):
                left = 1 if i == 0 else nums[i-1]
                right = 1 if i == len(nums) - 1 else nums[i+1]
                point = left * nums[i] * right
                # 做选择
                temp = nums[i]
                del nums[i]  # 在nums中删除元素 nums[i]
                # 递归回溯
                backtrack(nums, score + point)
                # 撤销选择
                nums.insert(i, temp)
        backtrack(nums, 0)
        return res

    def maxCoins2(self, nums) -> int:
        # 这个问题中我们每戳破一个气球 nums[i]，得到的分数和该气球相邻的气球 nums[i-1] 和 nums[i+1] 是有相关性的。
        # 运用动态规划算法的一个重要条件：子问题必须独立。
        # 所以对于这个戳气球问题，如果想用动态规划，必须巧妙地定义dp数组的含义，避免子问题产生相关性，才能推出合理的状态转移方程。
        #    那么我们可以改变问题：在一排气球 points 中，请你戳破气球 0 和气球 n+1 之间的所有气球（不包括 0 和 n+1），
        #    使得最终只剩下气球 0 和气球 n+1 两个气球，最多能够得到多少分？

        # 动态规划
        # dp[i][j] = x 的定义：戳破气球 i 和气球 j 之间（开区间，不包括 i 和 j）的所有气球，可以获得的最高分数为 x
        # 状态转移方程：
        #    dp[i][j] = max(dp[i][j],
        #                   dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        # 你不是要最后戳破气球 k 吗？
        #    那得先把开区间 (i, k) 的气球都戳破，再把开区间 (k, j) 的气球都戳破；
        #    最后剩下的气球 k，相邻的就是气球 i 和气球 j，这时候戳破 k 的话得到的分数就是 nums[i]*nums[k]*nums[j]。
        # 那么戳破开区间 (i, k) 和开区间 (k, j) 的气球最多能得到的分数是多少呢？
        #    嘿嘿，就是 dp[i][k] 和 dp[k][j]，这恰好就是我们对 dp 数组的定义嘛！
        n = len(nums)
        # 添加两侧的虚拟气球
        nums.insert(0, 1)
        nums.append(1)
        # base case 已经都被初始化为 0
        dp = [[0]*(n+2) for _ in range(n+2)]
        # 开始状态转移
        # i 应该从下往上
        for i in range(n, -1, -1):
            # j 应该从左往右
            for j in range(i+1, n+2):
                # 最后戳破的气球是哪个？
                for k in range(i+1, j):
                    # 择优做选择
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k]
                    )
        return dp[0][n + 1]


if __name__ == '__main__':
    # case1  res = 167
    # 解释：
    # nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    # coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
    nums1 = [3, 1, 5, 8]

    # case2  res = 10
    nums2 = [1, 5]

    sol = Solution()
    res1_1, res1_2 = sol.maxCoins1(nums1), sol.maxCoins2(nums1)
    res2_1, res2_2 = sol.maxCoins1(nums2), sol.maxCoins2(nums2)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)