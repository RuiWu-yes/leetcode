# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 44 通配符匹配
# @Content : 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#               '?' 可以匹配任何单个字符。
#               '*' 可以匹配任意字符串（包括空字符串）。
#            两个字符串完全匹配才算匹配成功。
#      说明 : 1) s 可能为空，且只包含从 a-z 的小写字母。
#            2) p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划
        # dp[i][j]的定义:【p从0位置到i位置】这一整段，是否能与【s从0位置到j位置】这一整段匹配
        # i(p, 行), j(s, 列)
        # 比如:
        # 0代表False, 1代表True
        #       '' a d c e b
        #    ''  1 0 0 0 0 0
        #     a  0 1 0 0 0 0
        #     *  0 1 1 1 1 1
        #     e  0 0 0 0 1 0
        #     ?  0 0 0 0 0 1
        m, n = len(p), len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            # p[i-1] == '*'的情况：要使dp[i][j]为True, 先决条件必须dp[i-1][k]为True,由于'*'的作用是可以匹配任何字符串
            if p[i - 1] == '*':
                # 此步骤是查找前一个状态dp[i-1][k]是否有True
                #     如果没找到，不做任何操作
                #     如果找到，则从此 k 直到 n 所有的dp[i][k]都为True
                k = 0
                while k < n + 1:
                    if dp[i - 1][k]: break
                    k += 1
                while k < n + 1:
                    dp[i][k] = True
                    k += 1
                continue
            for j in range(1, n + 1):
                # 要使dp[i][j]为True, 先决条件必须dp[i-1][j-1]为True
                #    要么p[i - 1] == '?'
                #    要么p[i - 1] == s[j - 1]
                if dp[i - 1][j - 1] and (p[i - 1] == "?" or p[i - 1] == s[j - 1]):  # 先判断字母是否符合
                    dp[i][j] = True
        return dp[m][n]


if __name__ == '__main__':
    # case1  res = false
    # 解释: "a" 无法匹配 "aa" 整个字符串。
    s1 = "aa"
    p1 = "a"

    # case2  res = true
    # 解释: '*' 可以匹配任意字符串。
    s2 = "aa"
    p2 = "*"

    # case3  res = false
    # 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
    s3 = "cb"
    p3 = "?a"

    # case4  res = true
    # 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
    s4 = "adceb"
    p4 = "*a*b"

    # case5  res = false
    s5 = "acdcb"
    p5 = "a*c?b"

    sol = Solution()
    res1 = sol.isMatch(s1, p1)
    res2 = sol.isMatch(s2, p2)
    res3 = sol.isMatch(s3, p3)
    res4 = sol.isMatch(s4, p4)
    res5 = sol.isMatch(s5, p5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)