# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 151 翻转字符串里的单词
# @Content : 给定一个字符串，逐个翻转字符串中的每个单词。
#      说明 : 无空格字符构成一个 单词 。
#            输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#            如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#      进阶 : 请尝试使用 O(1) 额外空间复杂度的原地解法。
import re


class Solution:
    def reverseWords1(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseWords2(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i + 1: j] + ' '
                while s[i] == ' ': i -= 1
                j = i + 1
            i -= 1
        return res + s[:j]

    def reverseWords3(self, s: str) -> str:
        # 正则匹配
        return ' '.join(re.findall('[^ ]+', s)[::-1])


if __name__ == '__main__':
    # case1  res = "blue is sky the"
    s1 = "the sky is blue"

    # case2  res = "world! hello"
    # 解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    s2 = "  hello world!  "

    # case3  res = "example good a"
    # 解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
    s3 = "a good   example"

    # case4  res = "Alice Loves Bob"
    s4 = "  Bob    Loves  Alice   "

    # case5  res = "bob like even not does Alice"
    s5 = "Alice does not even like bob"

    sol = Solution()
    res1 = sol.reverseWords1(s1), sol.reverseWords2(s1), sol.reverseWords3(s1)
    res2 = sol.reverseWords1(s2), sol.reverseWords2(s2), sol.reverseWords3(s2)
    res3 = sol.reverseWords1(s3), sol.reverseWords2(s3), sol.reverseWords3(s3)
    res4 = sol.reverseWords1(s4), sol.reverseWords2(s4), sol.reverseWords3(s4)
    res5 = sol.reverseWords1(s5), sol.reverseWords2(s5), sol.reverseWords3(s5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)