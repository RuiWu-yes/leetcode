# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 392 判断子序列
# @Content : 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#            字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
#            （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#      进阶： 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 利用双指针 i, j 分别指向 s, t，一边前进一边匹配子序列
        # 时间复杂度只需 O(N)
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)  # i能够走到底，说明s在t的子序列中

    def isSubsequence1(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        # 对 t 进行预处理
        index = defaultdict(list)
        for i in range(n):
            c = t[i]
            index[c].append(i)
        # 串 t 上的指针
        j = 0
        # 借助 index 查找 s[i]
        for i in range(m):
            c = s[i]
            # 整个 t 压根儿没有字符 c
            if not index[c]: return False
            pos = self.left_bound(index[c], j)
            # 二分搜索区间中没有找到字符
            # 比如：array = [0, 1, 2], target = 3, 此时 pos = 3，array长度 = 3
            if pos == len(index[c]): return False
            # 向前移动指针 j
            j = index[c][pos] + 1
        return True

    def left_bound(self, array, target):
        # 查找左侧边界的二分查找
        # 当 target 不存在时，得到的索引恰好是比 target 大的最小元素索引。
        lo, hi = 0, len(array)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > array[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    # case1  res = true
    s1 = "abc"
    t1 = "ahbgdc"

    # case2  res = false
    s2 = "axc"
    t2 = "ahbgdc"

    sol = Solution()
    res1 = sol.isSubsequence1(s1, t1)
    res2 = sol.isSubsequence1(s2, t2)
    print('case1:', res1)
    print('case2:', res2)