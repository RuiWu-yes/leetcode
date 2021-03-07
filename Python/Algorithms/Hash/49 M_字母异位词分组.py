# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 49 字母异位词分组
# @Content : 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # 哈希算法
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # 26个英文字母
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # 哈希算法
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())


if __name__ == '__main__':
    # case1  res = [["ate","eat","tea"], ["nat","tan"],["bat"]]
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    sol = Solution()
    res1 = sol.groupAnagrams1(strs1), sol.groupAnagrams2(strs1)
    print('case1:', res1)