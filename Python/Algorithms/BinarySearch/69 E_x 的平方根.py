# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 69 x 的平方根
# @Content : 实现 int sqrt(int x) 函数。
#            计算并返回 x 的平方根，其中 x 是非负整数。
#            由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        # 思路: 当 x >= 2 时，它的整数平方根一定小于 x / 2 且大于0，即 0 < a < x/2 。由于a一定是整数，
        #      此问题可以转换成有序整数数集中寻找一个特定值，因此可以使用二分法
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right


if __name__ == '__main__':
    # case1  res = 2
    x1 = 4

    # case2  res = 2
    # 说明: 8 的平方根是 2.82842...,
    #      由于返回类型是整数，小数部分将被舍去。
    x2 = 8

    sol = Solution()
    res1 = sol.mySqrt(x1)
    res2 = sol.mySqrt(x2)
    print('case1:', res1)
    print('case2:', res2)