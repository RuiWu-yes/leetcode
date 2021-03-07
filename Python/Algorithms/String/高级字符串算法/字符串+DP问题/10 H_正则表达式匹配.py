# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 10 正则表达式匹配
# @Content : 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#            '.' 匹配任意单个字符
#            '*' 匹配零个或多个前面的那一个元素
#            所谓匹配，是要涵盖 整个 字符串s的，而不是部分字符串。


class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        # 暴力解法
        if not p: return not s
        first = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch1(s, p[2:]) or first and self.isMatch1(s[1:], p)
        else:
            return first and self.isMatch1(s[1:], p[1:])

    def isMatch2(self, s: str, p: str) -> bool:
        # 动态规划:带备忘录的递归解法
        # 使用两个变量 i, j 记录当前匹配到的位置，从而避免使用子字符串切片，并且将 i, j 存入备忘录，避免重复计算即可
        memo = dict()  # 备忘录
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)


if __name__ == '__main__':
    # case1  res = false
    # 解释："a" 无法匹配 "aa" 整个字符串。
    s1 = "aa"
    p1 = "a"

    # case2  res = true
    # 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
    s2 = "aa"
    p2 = "a*"

    # case3  res = true
    # 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
    s3 = "ab"
    p3 = ".*"

    # case4  res = true
    # 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
    s4 = "aab"
    p4 = "c*a*b"

    # case5  res = false
    s5 = "mississippi"
    p5 = "mis*is*p*."

    sol = Solution()
    res1_1, res1_2 = sol.isMatch1(s1, p1), sol.isMatch2(s1, p1)
    res2_1, res2_2 = sol.isMatch1(s2, p2), sol.isMatch2(s2, p2)
    res3_1, res3_2 = sol.isMatch1(s3, p3), sol.isMatch2(s3, p3)
    res4_1, res4_2 = sol.isMatch1(s4, p4), sol.isMatch2(s4, p4)
    res5_1, res5_2 = sol.isMatch1(s5, p5), sol.isMatch2(s5, p5)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)
    print('case3:', res3_1, res3_2)
    print('case4:', res4_1, res4_2)
    print('case5:', res5_1, res5_2)