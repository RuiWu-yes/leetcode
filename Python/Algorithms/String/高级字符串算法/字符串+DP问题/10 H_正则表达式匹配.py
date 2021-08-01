# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 10 正则表达式匹配
# @Content : 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#            '.' 匹配任意单个字符
#            '*' 匹配零个或多个前面的那一个元素
#            所谓匹配，是要涵盖 整个 字符串s的，而不是部分字符串。


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 暴力解法
        if not p: return not s  # p为空，跟任何不为空的s都能匹配上
        # 1) 处理 '.'
        first = bool(s) and p[0] in {s[0], '.'}  # (s不为空) 并且 (p的首字符与s的首字符相等 或者 p的首字符为'.')
        # 2) 处理 '*'
        if len(p) >= 2 and p[1] == '*':  # (p的长度 >= 2) 并且 (p[1]为'*')
            # 如果发现有字符和'*'结合: 1) 匹配该字符0次，然后跳过该字符和‘*’ 或者 2) 当p[0]和s[0]匹配后，移动到 s
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            # 否则都是字符： 当p[0]和s[0]匹配后，移动到 s 和 p
            return first and self.isMatch(s[1:], p[1:])

    def isMatch1(self, s: str, p: str) -> bool:
        # 动态规划
        # dp[i][j]的定义：s[:i] 与 p[:j] 能否匹配
        # i(s, 行), j(p, 列)
        m, n = len(s), len(p)
        def matches(i: int, j: int) -> bool:
            # i, j状态时，是否匹配
            if i == 0:  # 此时对应着s == ''的情况，除非p也为''(i, j都为0)，否则任何一个不为空的p去匹配空s都为False
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 状态初始化
        dp[0][0] = True  # 表示s和p都为空的时候，可以匹配
        for i in range(m + 1):
            for j in range(1, n + 1):  # j为什么从1开始，是因为要保证j - 1 >= 0
                if p[j - 1] == '*':  # 出现'*'说明前面一定有字符，因此总是两个字符(比如：s*)出现
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]  # '*'匹配至少 1 次, 需要看一下(s)i-1的状态
                    dp[i][j] |= dp[i][j - 2]  # '*'匹配 0 次，即不管'*'前一个字符
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]

    def isMatch2(self, s: str, p: str) -> bool:
        # 动态规划:带备忘录的递归解法
        # 使用两个变量 i, j 记录当前匹配到的位置，从而避免使用子字符串切片，并且将 i, j 存入备忘录，避免重复计算即可
        memo = dict()  # 备忘录
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)  # j 到末尾了，i 也到末尾了
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
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
    res1 = sol.isMatch(s1, p1), sol.isMatch1(s1, p1), sol.isMatch2(s1, p1)
    res2 = sol.isMatch(s2, p2), sol.isMatch1(s2, p2), sol.isMatch2(s2, p2)
    res3 = sol.isMatch(s3, p3), sol.isMatch1(s3, p3), sol.isMatch2(s3, p3)
    res4 = sol.isMatch(s4, p4), sol.isMatch1(s4, p4), sol.isMatch2(s4, p4)
    res5 = sol.isMatch(s5, p5), sol.isMatch1(s5, p5), sol.isMatch2(s5, p5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)