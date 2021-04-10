# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 712 两个字符串的最小ASCII删除和
# @Content : 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 231
    # 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
    #      在 "eat" 中删除 "t" 并将 116 加入总和。
    #      结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
    s1_1, s2_1 = "sea", "eat"

    # case2  res = 403
    # 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
    # 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
    # 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
    # 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
    s1_2, s2_2 = "delete", "leet"

    sol = Solution()
    res1 = sol.minimumDeleteSum(s1_1, s2_1)
    res2 = sol.minimumDeleteSum(s1_2, s2_2)
    print('case1:', res1)
    print('case2:', res2)