# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 516 最长回文子序列
# @Content : 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp数组全部初始化为0
        # dp数组的定义：在子串 s[i..j] 中，最长回文子序列的长度为 dp[i][j]
        dp = [[0]*n for _ in range(n)]
        # base case
        for i in range(n):
            dp[i][i] = 1
        # 反着遍历保证正确的状态转移
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 如果它俩相等，那么它俩加上 s[i+1..j-1] 中的最长回文子序列就是 s[i..j] 的最长回文子序列
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                # 如果它俩不相等，说明它俩不可能同时出现在 s[i..j] 的最长回文子序列中，那么把它俩分别加入 s[i+1..j-1] 中，
                # 看看哪个子串产生的回文子序列更长即可
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # 整个 s 的最长回文子串长度
        return dp[0][n-1]


if __name__ == '__main__':
    # case1  res = 4
    s1 = "bbbab"

    # case2  res = 2
    s2 = "cbbd"

    sol = Solution()
    res1 = sol.longestPalindromeSubseq(s1)
    res2 = sol.longestPalindromeSubseq(s2)
    print('case1:', res1)
    print('case2:', res2)