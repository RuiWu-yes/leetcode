# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1312 让字符串成为回文串的最少插入次数
# @Content : 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#            请你返回让 s 成为回文串的最少操作次数。
#           「回文串」是正读和反读都相同的字符串。


class Solution:
    def minInsertions1(self, s: str) -> int:
        # 动态规划:带备忘录的递归解法
        memo = dict()
        def dp(i, j):
            # s[i, j]最少插入多少字符
            if (i, j) in memo:return memo[(i, j)]
            if i >= j: return 0
            if s[i] == s[j]:
                memo[(i, j)] = dp(i+1, j-1)
            else:
                memo[(i, j)] = min(dp(i+1, j), dp(i, j-1)) + 1
            return memo[(i, j)]
        return dp(0, len(s) - 1)

    def minInsertions2(self, s: str) -> int:
        # 动态规划: 时间和空间复杂度都是 O(N^2)
        n = len(s)
        # 定义：对 s[i..j]，最少需要插入 dp[i][j] 次才能变成回文
        # 我们定义一个二维的 dp 数组，dp[i][j] 的定义如下：对字符串 s[i..j]，最少需要进行 dp[i][j] 次插入才能变成回文串。
        dp = [[0]*n for _ in range(n)]
        # base case：i == j 时 dp[i][j] = 0，单个字符本身就是回文
        # dp 数组已经全部初始化为 0，base case 已初始化
        # 从下向上遍历
        for i in range(n-2, -1, -1):
            # 从左向右遍历
            for j in range(i+1, n):
                # 根据 s[i] 和 s[j] 进行状态转移
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        # 根据 dp 数组的定义，题目要求的答案
        return dp[0][n - 1]

    def minInsertions3(self, s: str) -> int:
        # 动态规划:状态压缩
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            # 记录 dp[i+1][j-1]
            pre = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    # dp[i][j] = dp[i+1][j-1]
                    dp[j] = pre
                else:
                    # dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
                    dp[j] = min(dp[j], dp[j-1]) + 1
                pre = temp
        return dp[n-1]


if __name__ == '__main__':
    # case1  res = 0
    # 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
    s1 = "zzazz"

    # case2  res = 2
    # 解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
    s2 = "mbadm"

    # case3  res = 5
    # 解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
    s3 = "leetcode"

    # case4  res = 0
    s4 = "g"

    # case5  res = 1
    s5 = "no"

    sol = Solution()
    res1_1, res1_2, res1_3 = sol.minInsertions1(s1), sol.minInsertions2(s1), sol.minInsertions3(s1)
    res2_1, res2_2, res2_3 = sol.minInsertions1(s2), sol.minInsertions2(s2), sol.minInsertions3(s2)
    res3_1, res3_2, res3_3 = sol.minInsertions1(s3), sol.minInsertions2(s3), sol.minInsertions3(s3)
    res4_1, res4_2, res4_3 = sol.minInsertions1(s4), sol.minInsertions2(s4), sol.minInsertions3(s4)
    res5_1, res5_2, res5_3 = sol.minInsertions1(s5), sol.minInsertions2(s5), sol.minInsertions3(s5)
    print('case1:', res1_1, res1_2, res1_3)
    print('case2:', res2_1, res2_2, res2_3)
    print('case3:', res3_1, res3_2, res3_3)
    print('case4:', res4_1, res4_2, res4_3)
    print('case5:', res5_1, res5_2, res5_3)