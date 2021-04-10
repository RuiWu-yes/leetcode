# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 72 编辑距离
# @Content : 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#            你可以对一个单词进行如下三种操作：
#               插入一个字符
#               删除一个字符
#               替换一个字符


class Solution:
    def minDistance1(self, word1: str, word2: str) -> int:
        # 暴力解法：不带备忘录的递归解法，会有重叠子问题
        def dp(i, j):
            # base case
            if i == -1: return j + 1  # i == -1可以认为此时的word1[-1] == ''(空字符),空字符变word2[j],则需要j+1次添加操作
            if j == -1: return i + 1  # j == -1可以认为此时的word2[-1] == ''(空字符),word1[i]变成空字符，则需要i+1次删除操作

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)          # 啥都不做
            else:
                return min(dp(i, j - 1) + 1,     # 插入
                           dp(i - 1, j) + 1,     # 删除
                           dp(i - 1, j - 1) + 1  # 替换
                           )
        # i, j初始化指向最后一个索引
        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        # 动态规划：带备忘录的递归解法
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # base case
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:  # 啥都不做
                memo[(i, j)] = dp(i - 1, j - 1)
            else:  # 每个状态进行转移时候，可以从插入、删除、替换三种操作任选一个
                memo[(i, j)] = min(dp(i, j - 1) + 1,
                                   dp(i - 1, j) + 1,
                                   dp(i - 1, j - 1) + 1
                                   )
            return memo[(i, j)]
        # i, j初始化指向最后一个索引
        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance3(self, word1: str, word2: str) -> int:
        # 动态规划：DP table
        m, n = len(word1), len(word2)
        # DP table初始化
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:  # 啥都不做
                    dp[i][j] = dp[i-1][j-1]
                else:  # 每个状态进行转移时候，可以从插入、删除、替换三种操作任选一个
                    dp[i][j] = min(dp[i-1][j] + 1,
                                   dp[i][j-1] + 1,
                                   dp[i-1][j-1] + 1
                                   )
        # 储存着整个word1和word2的最小编辑距离
        return dp[m][n]


if __name__ == '__main__':
    # case1  res = 3
    # 解释：
    # horse -> rorse (将 'h' 替换为 'r')
    # rorse -> rose (删除 'r')
    # rose -> ros (删除 'e')
    word1_1 = "horse"
    word2_1 = "ros"

    # case2  res = 5
    # intention -> inention (删除 't')
    # inention -> enention (将 'i' 替换为 'e')
    # enention -> exention (将 'n' 替换为 'x')
    # exention -> exection (将 'n' 替换为 'c')
    # exection -> execution (插入 'u')
    word1_2 = "intention"
    word2_2 = "execution"

    sol = Solution()
    res1 = sol.minDistance1(word1_1, word2_1), sol.minDistance2(word1_1, word2_1), sol.minDistance3(word1_1, word2_1)
    res2 = sol.minDistance1(word1_2, word2_2), sol.minDistance2(word1_2, word2_2), sol.minDistance3(word1_2, word2_2)
    print('case1:', res1)
    print('case2:', res2)