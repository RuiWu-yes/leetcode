# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 28 实现 strStr()
# @Content : 实现 strStr() 函数。
#            给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle
#            字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。


class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        # 暴力匹配
        M, N = len(needle), len(haystack)
        for i in range(N - M + 1):
            temp = -1
            for j in range(M):
                if needle[j] != haystack[i+j]:
                    break
                temp = j
            # needle 全都匹配了
            if temp == M-1: return i
        # haystack 中不存在 needle 子串
        return -1

    def __init__(self):
        self.dp = [[]]
        self.pat = ''

    def KMP(self, pat):
        self.pat = pat
        M = len(pat)
        dp = [[0]*M for _ in range(256)]  # dp[状态][字符] = 下个状态
        # base case
        dp[0][pat[0]] = 1
        # 影子状态 X 初始为 0
        X = 0
        # 构建状态转移图（稍改的更紧凑了）
        for j in range(1, M):
            for c in range(256):
                dp[j][c] = dp[X][c]
                dp[j][pat[j]] = j + 1
                # 更新影子状态
                X = dp[X][pat[j]]

    def strStr(self, haystack: str, needle: str) -> int:
        M, N = len(needle), len(haystack)
        # pat 的初始态为 0
        j = 0
        for i in range(N):
            # 计算 pat 的下一个状态
            j = dp[j][haystack[i]]
            # 到达终止态，返回结果
            if j == M:
                return i - M + 1
        # 没到达终止态，匹配失败
        return -1


if __name__ == '__main__':
    # case1  res = 2
    haystack1 = "hello"
    needle1 = "ll"

    # case2  res = -1
    haystack2 = "aaaaa"
    needle2 = "bba"

    sol = Solution()
    res1 = sol.strStr1(haystack1, needle1)
    res2 = sol.strStr1(haystack2, needle2)
    print('case1:', res1)
    print('case2:', res2)