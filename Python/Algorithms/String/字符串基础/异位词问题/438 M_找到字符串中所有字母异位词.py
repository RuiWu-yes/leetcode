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
        # 滑动窗口
        res = []
        need, window = Counter(p), defaultdict(lambda: 0)
        # 初始化窗口左右边界为s最左侧
        # valid记录窗口中有几个所需字符满足异位词条件，初始为0
        left, right, valid = 0, 0, 0
        while right < len(s):
            # 移动窗口右边界(移动一次，更新一次窗口信息)
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # valid等于need的长度, 说明此时所需字符都满足异位词条件
            #    首先判断窗口长度(right - left)是否等于p的长度，如果等于则说明此时的窗口中的字符串是p的字母异位词
            #    再移动窗口左边界(移动一次，更新一次窗口信息)
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
    s1 = "cbaebabacd"
    p1 = "abc"

    # case2  res = [0, 1, 2]
    # 解释:
    #     起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词.
    #     起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词.
    #     起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词.
    s2 = "abab"
    p2 = "ab"

    # case3  res = [1]
    s3 = "baa"
    p3 = "aa"

    sol = Solution()
    res1 = sol.findAnagrams(s1, p1)
    res2 = sol.findAnagrams(s2, p2)
    res3 = sol.findAnagrams(s3, p3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)