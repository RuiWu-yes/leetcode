# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 567 字符串的排列
# @Contect : 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#            换句话说，第一个字符串的排列之一是第二个字符串的子串。
from collections import defaultdict
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口
        need, window = Counter(s1), defaultdict(lambda: 0)
        left, right, valid = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left >= len(s1):
                if valid == len(need):  # 在这里判断是否找到了合法的子串
                    return True
                d = s2[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # 未找到符合条件的子串
        return False


if __name__ == '__main__':
    # # case1  res = True
    # s1 = "ab"
    # s2 = "eidbaooo"

    # case2  res = False
    s1 = "ab"
    s2 = "eidboaoo"

    sol = Solution()
    res = sol.checkInclusion(s1, s2)
    print(res)