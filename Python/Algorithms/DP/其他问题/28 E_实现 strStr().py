# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 28 实现 strStr()
# @Content : 实现 strStr() 函数。
#            给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle
#            字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 2
    haystack1 = "hello"
    needle1 = "ll"

    # case2  res = -1
    haystack2 = "aaaaa"
    needle2 = "bba"

    sol = Solution()
    res1 = sol.strStr(haystack1, needle1)
    res2 = sol.strStr(haystack2, needle2)
    print('case1:', res1)
    print('case2:', res2)