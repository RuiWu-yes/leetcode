# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 5 最长回文子串
# @Content : 给你一个字符串 s，找到 s 中最长的回文子串。


class Solution:
    def longestPalindrome1(self, s: str) -> str:
        # 动态规划
        # dp[i][j]的定义：子串 s[i..j] 是否为回文子串，这里子串 s[i..j] 定义为左闭右闭区间，可以取到 s[i] 和 s[j]
        # 状态转移方程：
        #    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        # 说明：
        #    1)「动态规划」事实上是在填一张二维表格，由于构成子串，因此 i 和 j 的关系是 i <= j ，因此，只需要填这张表格对角线以上的部分。
        #    2) 看到 dp[i + 1][j - 1] 就得考虑边界情况。
        # ->边界条件是：表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。
        #   这个结论很显然：j - i < 3 等价于 j - i + 1 < 4，即当子串 s[i..j] 的长度等于 2 或者等于 3 的时候，其实只需要判断
        #   一下头尾两个字符是否相等就可以直接下结论了。
        # ->如果子串 s[i + 1..j - 1] 只有 1 个字符，即去掉两头，剩下中间部分只有 11 个字符，显然是回文；
        # ->如果子串 s[i + 1..j - 1] 为空串，那么子串 s[i, j] 一定是回文子串。
        # ->因此，在 s[i] == s[j] 成立和 j - i < 3 的前提下，直接可以下结论，dp[i][j] = true，否则才执行状态转移。
        # 可以发现：
        #   1、当 i 和 j (图中是 l 和 r) 的差距等于小于 3 的时候，dp 值可以直接判断，不用参考以前的 dp 值；
        #   2、其它情况，每当计算新 dp 值的时候，都一定会参考「左下角」的 dp 值，即 dp[i + 1][j - 1]（i + 1 表示在下边，j - 1 表示在左边）。
        #   因此，从上到下写，或者从下到上写，都是可以的。
        dp = [[False] * len(s) for _ in range(len(s))]
        res = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if res == "" or max_length < j - i + 1:
                        res = s[i:j+1]
                        max_length = j - i + 1
        return res

    def longestPalindrome2(self, s: str) -> str:
        # 中心扩散法
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


if __name__ == '__main__':
    # case1  res = "bab" or "aba"
    # 解释："aba" 同样是符合题意的答案。
    s1 = "babad"

    # case2  res = "bb"
    s2 = "cbbd"

    # case3  res = "a"
    s3 = "a"

    # case4  res = "a"
    s4 = "ac"

    sol = Solution()
    res1 = sol.longestPalindrome1(s1), sol.longestPalindrome2(s1)
    res2 = sol.longestPalindrome1(s2), sol.longestPalindrome2(s2)
    res3 = sol.longestPalindrome1(s3), sol.longestPalindrome2(s3)
    res4 = sol.longestPalindrome1(s4), sol.longestPalindrome2(s4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)