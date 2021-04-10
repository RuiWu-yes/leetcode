# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 583 两个字符串的删除操作
# @Content : 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
#            每步可以删除任意一个字符串中的一个字符。


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 动态规划：求最长公共子序列的长度
        # dp[i][j]的定义：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]
        # 状态转移：
        #    用两个指针 i 和 j 从后往前遍历 s1 和 s2，如果 s1[i]==s2[j]，那么这个字符一定在 lcs 中；
        #    否则的话，s1[i] 和 s2[j] 这两个字符至少有一个不在 lcs 中，需要丢弃一个。
        m, n = len(word1), len(word2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[-1][-1]
        return m - lcs + n - lcs


if __name__ == '__main__':
    # case1  res = 2
    # 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
    word1, word2 = "sea", "eat"

    sol = Solution()
    res = sol.minDistance(word1, word2)
    print('case1:', res)