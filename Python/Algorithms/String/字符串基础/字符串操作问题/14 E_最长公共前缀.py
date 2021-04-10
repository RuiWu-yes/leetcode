# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 14 最长公共前缀
# @Content : 编写一个函数来查找字符串数组中的最长公共前缀。
#            如果不存在公共前缀，返回空字符串 ""。
from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        # 取每个单词的同一位置的字母，看是否相同
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # 取一个单词s, 和后面单词比较，看 s 与每个单词相同的最长前缀是多少
        if not strs:
            return ""
        res = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res


if __name__ == '__main__':
    # case1  res = "fl"
    strs1 = ["flower", "flow", "flight"]

    # case2  res = ""
    # 解释：输入不存在公共前缀。
    strs2 = ["dog", "racecar", "car"]

    sol = Solution()
    res1 = sol.longestCommonPrefix1(strs1), sol.longestCommonPrefix2(strs1)
    res2 = sol.longestCommonPrefix1(strs2), sol.longestCommonPrefix2(strs2)
    print('case1:', res1)
    print('case2:', res2)