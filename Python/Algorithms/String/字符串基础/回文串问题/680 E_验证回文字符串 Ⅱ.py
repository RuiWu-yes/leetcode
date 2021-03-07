# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 680 验证回文字符串 Ⅱ
# @Content : 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#      注意 : 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 双指针法
        if s == s[::-1]:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                a = s[:left] + s[left+1:]
                if a == a[::-1]:
                    return True
                b = s[:right] + s[right+1:]
                if b == b[::-1]:
                    return True
                return False
            else:
                left += 1
                right -= 1
        return False


if __name__ == '__main__':
    # case1  res = true
    s1 = "aba"

    # case2  res = true
    # 解释: 你可以删除c字符。
    s2 = "abca"

    sol = Solution()
    res1 = sol.validPalindrome(s1)
    res2 = sol.validPalindrome(s2)
    print('case1:', res1)
    print('case2:', res2)