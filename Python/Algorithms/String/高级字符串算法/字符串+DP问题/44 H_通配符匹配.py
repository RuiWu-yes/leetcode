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
        # dp[m][n]的定义:【p从0位置到m位置】这一整段，是否能与【s从0位置到n位置】这一整段匹配
        # s横，p纵
        zong = len(p) + 1  # 纵轴长度
        heng = len(s) + 1  # 横轴长度
        dp = [[False] * heng for _ in range(zong)]
        dp[0][0] = True
        for m in range(1, zong):
            if p[m - 1] == '*':
                j = 0
                while j < heng:
                    if dp[m - 1][j] == True:
                        break
                    j += 1
                while j < heng:
                    dp[m][j] = True
                    j += 1
                continue
            for n in range(1, heng):
                if dp[m - 1][n - 1] and (p[m - 1] == "?" or p[m - 1] == s[n - 1]):  # 先判断字母是否符合
                    dp[m][n] = True
        return dp[zong - 1][heng - 1]


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
