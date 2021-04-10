# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 392 判断子序列
# @Content : 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#            字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
#            （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#      进阶： 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass


if __name__ == '__main__':
    # case1  res = true
    s1 = "abc"
    t1 = "ahbgdc"

    # case2  res = false
    s2 = "axc"
    t2 = "ahbgdc"

    sol = Solution()
    res1 = sol.isSubsequence(s1, t1)
    res2 = sol.isSubsequence(s2, t2)
    print('case1:', res1)
    print('case2:', res2)