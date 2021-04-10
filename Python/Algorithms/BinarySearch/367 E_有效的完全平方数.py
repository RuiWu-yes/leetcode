# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 367 有效的完全平方数
# @Content : 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#     说明 ： 不要使用任何内置的库函数，如  sqrt。


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 二分法
        if num < 2:
            return True
        left, right = 2, num//2
        while left <= right:
            pivot = left + (right - left) // 2
            nums = pivot * pivot
            if nums > num:
                right = pivot - 1
            elif nums < num:
                left = pivot + 1
            else:
                return True
        return False


if __name__ == '__main__':
    # case1  res = true
    num1 = 16

    # case2  res = false
    num2 = 14