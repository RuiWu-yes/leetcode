# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 474 一和零
# @Content : 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#            请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
#            如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # 动态规划
        # 可用0和1的个数可以看成不同容量的背包(二维)
        # dp[i][j]的定义：dp[i][j]为 i, j 状态时最大子集的大小 (i 表示可用 0 的个数，j 表示可用的 1 的个数)
        # 对于可以放得下的背包  ①不放，则查看原旧背包容量　②放，则 1（当前01串）+ 变小的 旧背包容量
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 背包
        for string in strs:
            zero_count, one_count = string.count('0'), string.count('1')
            # 倒序遍历背包
            for i in range(m, zero_count - 1, -1):
                for j in range(n, one_count - 1, -1):
                    dp[i][j] = max(1 + dp[i - zero_count][j - one_count], dp[i][j])
        return dp[m][n]


if __name__ == '__main__':
    # case1  res = 4
    # 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
    # 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
    strs1 = ["10", "0001", "111001", "1", "0"]
    m1 = 5
    n1 = 3

    # case2  res = 2
    # 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
    strs2 = ["10", "0", "1"]
    m2 = 1
    n2 = 1

    sol = Solution()
    res1 = sol.findMaxForm(strs1, m1, n1)
    res2 = sol.findMaxForm(strs2, m2, n2)
    print('case1:', res1)
    print('case2:', res2)