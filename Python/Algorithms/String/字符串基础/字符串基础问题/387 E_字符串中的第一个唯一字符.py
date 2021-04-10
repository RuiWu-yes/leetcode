# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 387 字符串中的第一个唯一字符
# @Content : 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


class Solution:
    def firstUniqChar1(self, s: str) -> int:
        # 先假设最小索引为最后的字符索引
        min_unique_char_index = len(s)
        # 已知字符串由小写字母构成，则遍历a-z
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            # 分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
            if i != -1 and i == s.rfind(c):
                # 更新最新的最小索引
                min_unique_char_index = min(min_unique_char_index, i)
        # 如果返回值不为最后字符的索引，则返回最小索引值
        # 否则，根据题意，返回-1
        return min_unique_char_index if min_unique_char_index != len(s) else -1

    def firstUniqChar2(self, s: str) -> int:
        # 两次遍历：第一次对每个字符计数，第二次找到第一个计数为1的字符
        dic = {c: s.count(c) for c in set(s)}
        # 找到并返回首个满足出现次数为一的字符
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    # case1  res = 0
    s1 = "leetcode"

    # case2  res = 2
    s2 = "loveleetcode"

    sol = Solution()
    res1 = sol.firstUniqChar1(s1), sol.firstUniqChar2(s1)
    res2 = sol.firstUniqChar1(s2), sol.firstUniqChar2(s2)
    print('case1:', res1)
    print('case2:', res2)