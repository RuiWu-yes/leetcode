# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 5 最长回文子串
# @Content : 给你一个字符串 s，找到 s 中最长的回文子串。


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome1(self, s: str) -> str:
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

    def longestPalindrome2(self, s: str) -> str:
        # 动态规划
        dp = [[0] * len(s) for _ in range(len(s))]
        res = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if res == "" or max_length < j - i + 1:
                        res = s[i:j+1]
                        max_length = j - i + 1
        return res


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