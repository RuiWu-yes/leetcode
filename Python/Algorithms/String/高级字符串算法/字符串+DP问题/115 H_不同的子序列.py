# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 115 不同的子序列
# @Content : 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#            字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
#            （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#            题目数据保证答案符合 32 位带符号整数范围。


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 动态规划
        # dp[i][j]的定义： t(从 0 ~ i 字符串切片)在 s(从 0 ~ j 字符串切片)的子序列中出现的个数
        # 动态转移方程:
        #     对于第一行, t 为空,因为空集是所有字符串子集, 所以我们第一行都是 1
        #     对于第一列, s 为空,这样组成 t 个数当然为 0 了
        # 至于动态转移方程怎么得到,可以根据初始状态下的状态数组，去推理一下!
        #     当 s[j] == t[i] , dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        #     当 s[j] != t[i] , dp[i][j] = dp[i][j-1]
        # 比如：
        #       '' r o o b
        #    ''  1 1 1 1 1
        #     r  0 1 1 1 1
        #     o  0 0 1 2 2
        #     b  0 0 0 0 2
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # 状态初始化: t为空是任何s(包括为空)的子序列，所以dp[0][j] = 1
        for j in range(m + 1):
            dp[0][j] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    # case1  res = 3
    # 解释：
    # 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
    # (上箭头符号 ^ 表示选取的字母)
    # rabbbit
    # ^^^^ ^^
    # rabbbit
    # ^^ ^^^^
    # rabbbit
    # ^^^ ^^^
    s1 = "rabbbit"
    t1 = "rabbit"

    # case2  res = 5
    # 解释：
    # 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
    # (上箭头符号 ^ 表示选取的字母)
    # babgbag
    # ^^ ^
    # babgbag
    # ^^    ^
    # babgbag
    # ^    ^^
    # babgbag
    #   ^  ^^
    # babgbag
    #     ^^^
    s2 = "babgbag"
    t2 = "bag"

    sol = Solution()
    res1 = sol.numDistinct(s1, t1)
    res2 = sol.numDistinct(s2, t2)
    print('case1:', res1)
    print('case2:', res2)