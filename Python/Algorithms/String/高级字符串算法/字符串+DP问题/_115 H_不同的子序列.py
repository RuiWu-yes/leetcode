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
        # n(t, i, 行), m(s, j, 列)
        # 动态转移方程:
        #     对于第一行, t 为空,因为空集是所有字符串子集, 所以我们第一行都是 1
        #     对于第一列, s 为空,这样组成 t 个数当然为 0 了
        # 接下来的问题就是：我们怎么由子状态得到当前状态？ 对于这个问题，对于 dp[i][j], 即 s 的前 i 个字符中 t 的前 j 个字符出现的次数，
        # 我们需要分下面两种情况讨论：
        #   1) s[i] == t[j], 即当前字符相等，那么这个时候 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]，加法的两项分别对应着s的子串中
        #      保留s[i](s[i]对应 t[j], 这样的子串个数为dp[i-1][j-1]) 和 不保留s[i]两种情况
        #   2) s[i] != t[j], 即当前字符不等，那么删除字符后 s[i] 必定不能被保留， 所以 dp[i][j] = dp[i-1][j]，
        #      即: s 的前 i 个字符 中 t 的前 j 个字符出现的次数, 等于 s 的前 i-1 个字符 中 t 的前 j 个字符出现的次数
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