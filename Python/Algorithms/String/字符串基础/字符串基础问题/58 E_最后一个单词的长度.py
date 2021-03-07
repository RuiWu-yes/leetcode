# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 58 最后一个单词的长度
# @Content : 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。
#            如果不存在最后一个单词，请返回 0 。
#            单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。


class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        return len(s.strip().split()[-1]) if len(s.strip()) > 0 else 0

    def lengthOfLastWord2(self, s: str) -> int:
        end = len(s) - 1
        if end < 0: return 0
        while end >= 0 and s[end] == ' ':
            end -= 1
        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1
        return end - start


if __name__ == '__main__':
    # case1  res = 5
    s1 = "Hello World"

    # case2  res = 0
    s2 = " "

    sol = Solution()
    res1 = sol.lengthOfLastWord1(s1), sol.lengthOfLastWord2(s1)
    res2 = sol.lengthOfLastWord1(s2), sol.lengthOfLastWord2(s2)
    print('case1:', res1)
    print('case2:', res2)