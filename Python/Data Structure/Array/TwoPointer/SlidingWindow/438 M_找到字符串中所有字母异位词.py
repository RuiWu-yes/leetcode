# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 438 找到字符串中所有字母异位词
# @Content : 给定一个字符串 s 和一个非空字符串 p,找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引.
#            字符串只包含小写英文字母,并且字符串 s 和 p 的长度都不超过 20100.
# @explain : 字母异位词指字母相同，但排列不同的字符串;
#            不考虑答案输出的顺序.
from collections import defaultdict
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        need, window = Counter(p), defaultdict(lambda: 0)
        left, right, valid = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


if __name__ == '__main__':
    # case1  res = [0, 6]
    # 解释:
    #     起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词.
    #     起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词.
    s = "cbaebabacd"
    p = "abc"

    # # case2  res = [0, 1, 2]
    # # 解释:
    # #     起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词.
    # #     起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词.
    # #     起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词.
    # s = "abab"
    # p = "ab"

    # # case3  res = [1]
    # s = "baa"
    # p = "aa"

    sol = Solution()
    res = sol.findAnagrams(s, p)
    print(res)