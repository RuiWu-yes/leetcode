# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 32 最长有效括号
# @Content : 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        # 动态规划
        # dp[i]的定义: 以 i 结尾的最长有效括号
        # 状态转移：
        #   1. 当 s[i] 为 '(', dp[i] 必然等于 0，因为不可能组成有效的括号；
        #   2. 那么 s[i] 为 ')'
        #       2.1 当 s[i-1] 为 '('，那么 dp[i] = dp[i-2] + 2
        #       2.2 当 s[i-1] 为 ')' 并且 s[i-dp[i-1] - 1] 为 '('，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

    def longestValidParentheses2(self, s: str) -> int:
        # 使用栈
        if not s: return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


if __name__ == '__main__':
    # case1  res = 2
    # 解释：最长有效括号子串是 "()"
    s1 = "(()"

    # case2  res = 4
    # 解释：最长有效括号子串是 "()()"
    s2 = ")()())"

    # case3  res = 0
    s3 = ""

    sol = Solution()
    res1 = sol.longestValidParentheses1(s1), sol.longestValidParentheses2(s1)
    res2 = sol.longestValidParentheses1(s2), sol.longestValidParentheses2(s2)
    res3 = sol.longestValidParentheses1(s3), sol.longestValidParentheses2(s3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)