# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 416 分割等和子集
# @Content : 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# @Att     : 1) 每个数组中的元素不会超过 100
#            2) 数组的大小不会超过 200


class Solution:
    def canPartition1(self, nums) -> bool:
        # 动态规划：DP table
        # dp[i][j] = x 表示，对于前 i 个物品，当前背包的容量为 j 时，若 x 为 true，则说明可以恰好将背包装满，
        #                                                    若 x 为 false，则说明不能恰好将背包装满。
        # 如果不把 nums[i] 算入子集，或者说你不把这第 i 个物品装入背包，那么是否能够恰好装满背包，取决于上一个状态 dp[i-1][j]，继承之前的结果。
        # 如果把 nums[i] 算入子集，或者说你把这第 i 个物品装入了背包，那么是否能够恰好装满背包，取决于状态 dp[i-1][j-nums[i-1]]。
        m = sum(nums)
        if m % 2 == 1: return False  # 和为奇数时，不可能划分成两个和相等的集合
        n = len(nums)
        m = int(m / 2)
        dp = [[False]*(m+1) for _ in range(n+1)]
        # base case
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):  # 注意 i 是从 1 开始的，而数组索引是从 0 开始的，所以第 i 个物品的重量应该是 nums[i-1]
            for j in range(1, m+1):
                # 背包容量不足，不能装入第 i 个物品
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                # 装入或不装入背包
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]  # '|'：位运算符-或, 只要有一个为真就为真，否则为假
        return dp[n][m]

    def canPartition2(self, nums) -> bool:
        # 动态规划：DP table。状态压缩，空间复杂度从二维数组降为一维数组
        m = sum(nums)
        if m % 2 == 1: return False  # 和为奇数时，不可能划分成两个和相等的集合
        n = len(nums)
        m = int(m / 2)
        dp = [False for _ in range(m+1)]
        # base case
        dp[0] = True
        for i in range(n):
            for j in range(m, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] | dp[j-nums[i]]
        return dp[m]


if __name__ == '__main__':
    # case1  res = True
    # 解释: 数组可以分割成 [1, 5, 5] 和 [11].
    nums1 = [1, 5, 11, 5]

    # # case2  res = False
    # # 解释: 数组不能分割成两个元素和相等的子集.
    nums2 = [1, 2, 3, 5]

    sol = Solution()
    res1_1 = sol.canPartition1(nums1)
    res1_2 = sol.canPartition2(nums1)
    res2_1 = sol.canPartition2(nums2)
    res2_2 = sol.canPartition2(nums1)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)