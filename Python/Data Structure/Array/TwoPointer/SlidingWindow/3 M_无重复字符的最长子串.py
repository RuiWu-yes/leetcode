# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 3 无重复字符的最长子串
# @Content : 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(lambda: 0)
        left, right = 0, 0
        res = 0  # 记录结果
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            window[c] += 1
            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
            # 在这里更新答案
            res = max(res, right - left)
        return res


if __name__ == '__main__':
    # case1  res = 3
    # 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    s1 = "abcabcbb"

    # case2  res = 1
    # 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    s2 = "bbbbb"

    # case3  res = 3
    # 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    s3 = "pwwkew"

    # case4  res = 0
    s4 = ""

    sol = Solution()
    res1 = sol.lengthOfLongestSubstring(s1)
    res2 = sol.lengthOfLongestSubstring(s2)
    res3 = sol.lengthOfLongestSubstring(s3)
    res4 = sol.lengthOfLongestSubstring(s4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)