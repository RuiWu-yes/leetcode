# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 125 验证回文串
# @Content : 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#      说明 ：本题中，我们将空字符串定义为有效的回文串。


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        # filter(判断函数, 可迭代对象)
        s = list(filter(str.isalnum, s.lower()))
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        # 双指针法
        left, right = 0, len(s) - 1
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > -1 and not s[right].isalnum():
                right -= 1
            if left > right:
                return True
            if s[left].upper() != s[right].upper():
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    # case1  res = true
    s1 = "A man, a plan, a canal: Panama"

    # case2  res = false
    s2 = "race a car"

    sol = Solution()
    res1 = sol.isPalindrome1(s1), sol.isPalindrome2(s1)
    res2 = sol.isPalindrome1(s2), sol.isPalindrome2(s2)
    print('case1:', res1)
    print('case2:', res2)