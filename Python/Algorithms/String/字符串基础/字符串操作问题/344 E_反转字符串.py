# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 344 反转字符串
# @Content : 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#            不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#            你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
from typing import List


class Solution:
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针法
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s: List[str]) -> None:
        # 切片赋值(但不是原地操作)
        s[::] = s[::-1]

    def reverseString3(self, s: List[str]) -> None:
        # Python自带的reverse方法
        s.reverse()


if __name__ == '__main__':
    # case1  res = ["o","l","l","e","h"]
    s1 = ["h", "e", "l", "l", "o"]

    # case2  res = ["h","a","n","n","a","H"]
    s2 = ["H", "a", "n", "n", "a", "h"]

    sol = Solution()
    sol.reverseString1(s1)
    sol.reverseString1(s2)

    # sol.reverseString2(s1)
    # sol.reverseString2(s2)

    # sol.reverseString3(s1)
    # sol.reverseString3(s2)

    print('case1:', s1)
    print('case2:', s2)