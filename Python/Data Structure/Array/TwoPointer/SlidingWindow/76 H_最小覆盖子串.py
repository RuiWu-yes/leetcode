# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 76 最小覆盖子串
# @Contect : 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""。
from collections import defaultdict
from collections import Counter


class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        # 滑动窗口1
        need, window = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for str in t: need[str] += 1
        left, right, valid = 0, 0, 0
        start, length = 0, float('inf')  # 记录最小覆盖子串的起始索引及长度
        while right < len(s):
            c = s[right]  # c是将移入窗口的字符
            right += 1  # 右移窗口
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while valid == len(need):  # 当valid为t的长度时，说明包含了t中的所有字符。此时right停止，开始left更新
                # 在这里更新最小覆盖子串
                if right - left < length:  # 第一次length肯定小于float('inf')，更新新length，之后只要比现有length小就更新
                    start = left
                    length = right - left
                d = s[left]  # d是将移出窗口的字符
                left += 1  # 左移窗口
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start: start+length]

    def minWindow2(self, s: str, t: str) -> str:
        # 滑动窗口2
        need, window = Counter(t), defaultdict(lambda: 0)   # 使用Counter对字符串中的字符计数
        left, right, valid = 0, 0, 0
        start, length = 0, float('inf')  # 记录最小覆盖子串的起始索引及长度
        while right < len(s):
            c = s[right]  # c是将移入窗口的字符
            right += 1  # 右移窗口
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]  # d是将移出窗口的字符
                left += 1  # 左移窗口
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start: start+length]


if __name__ == '__main__':
    # case1  res = "BANC"
    s1 = "ADOBECODEBANC"
    t1 = "ABC"

    # case2  res = "a"
    s2 = "a"
    t2 = "a"

    # case3  res = ""
    s3 = 'a'
    t3 = 'aa'

    sol = Solution()
    res1 = sol.minWindow1(s1, t1), sol.minWindow2(s1, t1)
    res2 = sol.minWindow1(s2, t2), sol.minWindow2(s2, t2)
    res3 = sol.minWindow1(s3, t3), sol.minWindow2(s3, t3)
    print(res1)
    print(res2)
    print(res3)