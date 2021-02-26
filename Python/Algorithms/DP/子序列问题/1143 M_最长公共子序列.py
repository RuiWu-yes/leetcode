# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1143 最长公共子序列
# @Content : 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度.
#            若这两个字符串没有公共子序列，则返回 0.


class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        # 暴力解法：可以用备忘录去优化
        def dp(i, j):
            # 空串的base case
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                # 这边找到一个lcs的元素，继续往前找
                return dp(i-1, j-1) + 1
            else:
                # 谁能让lcs最长，就听谁的
                return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1)-1, len(text2)-1)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        # 动态规划：用DP table来优化时间复杂度
        # dp[i][j]的定义：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]
        # 状态转移：
        #    用两个指针 i 和 j 从后往前遍历 s1 和 s2，如果 s1[i]==s2[j]，那么这个字符一定在 lcs 中；
        #    否则的话，s1[i] 和 s2[j] 这两个字符至少有一个不在 lcs 中，需要丢弃一个。
        m, n = len(text1), len(text2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    # case1  res = 3
    # 最长公共子序列是 "ace",它的长度为 3.
    text1 = "abcde"
    text2 = "ace"

    # # case2  res = 3
    # # 最长公共子序列是 "abc",它的长度为 3.
    # text1 = "abc"
    # text2 = "abc"

    # # case3  res = 0
    # # 两个字符串没有公共子序列,返回 0.
    # text1 = "abc"
    # text2 = "def"

    sol = Solution()
    res1 = sol.longestCommonSubsequence1(text1, text2)
    res2 = sol.longestCommonSubsequence2(text1, text2)
    print(res1, res2)