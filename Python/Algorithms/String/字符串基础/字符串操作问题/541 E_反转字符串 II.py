# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 541 反转字符串 II
# @Content : 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
#               1) 如果剩余字符少于 k 个，则将剩余字符全部反转。
#               2) 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#      提示 : 该字符串只包含小写英文字母。
#            给定字符串的长度和 k 在 [1, 10000] 范围内。


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 切片法
        res = ''
        for i in range(0, len(s), 2*k):
            res += s[i:i+k][::-1] + s[i+k:i+2*k]
        return res


if __name__ == '__main__':
    # case1  res = "bacdfeg"
    s1 = "abcdefg"
    k1 = 2

    sol = Solution()
    res1 = sol.reverseStr(s1, k1)
    print('case1:', res1)
