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
        # dp[i][j] 的定义：对字符串 s[i..j]，最少需要进行 dp[i][j] 次插入才能变成回文串。
        # 状态转移就是从小规模问题的答案推导更大规模问题的答案，从 base case 向其他状态推导嘛。如果我们现在想计算 dp[i][j] 的值，
        # 而且假设我们已经计算出了子问题 dp[i+1][j-1] 的值了，你能不能想办法推出 dp[i][j] 的值呢？
        #    既然已经算出 dp[i+1][j-1]，即知道了 s[i+1..j-1] 成为回文串的最小插入次数，那么也就可以认为 s[i+1..j-1] 已经是一个回文串了，
        #    所以通过 dp[i+1][j-1] 推导 dp[i][j] 的关键就在于 s[i] 和 s[j] 这两个字符。
        #    1) 如果 s[i] == s[j] 的话，我们不需要进行任何插入，只要知道如何把 s[i+1..j-1] 变成回文串即可
        #    2) 如果 s[i] != s[j] 的话，无脑插入两次肯定是可以让 s[i..j] 变成回文串，但是不一定是插入次数最少的，最优的插入方案应该被拆解成如下流程：
        #       步骤1 做选择，先将 s[i..j-1] 或者 s[i+1..j] 变成回文串。怎么做选择呢？谁变成回文串的插入次数少，就选谁呗。
        #       步骤2 根据步骤1的选择，将 s[i..j] 变成回文
        n = len(s)
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
            pre = 0   # 每次换行，都要将pre置0 (因为向右遍历，pre就会记录一次。这样如果换行的时候，pre记录的就不是左相邻的值)
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
    res1 = sol.minInsertions1(s1), sol.minInsertions2(s1), sol.minInsertions3(s1)
    res2 = sol.minInsertions1(s2), sol.minInsertions2(s2), sol.minInsertions3(s2)
    res3 = sol.minInsertions1(s3), sol.minInsertions2(s3), sol.minInsertions3(s3)
    res4 = sol.minInsertions1(s4), sol.minInsertions2(s4), sol.minInsertions3(s4)
    res5 = sol.minInsertions1(s5), sol.minInsertions2(s5), sol.minInsertions3(s5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)