# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 69 x 的平方根
# @Content : 实现 int sqrt(int x) 函数。
#            计算并返回 x 的平方根，其中 x 是非负整数。
#            由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
import math


class Solution:
    def mySqrt1(self, x: int) -> int:
        # 袖珍计算器算法(时间复杂度：O(1), 空间复杂度：O(1))
        # 「袖珍计算器算法」是一种用指数函数 exp 和对数函数 In 代替平方根函数的方法。我们通过有限的可以使用的数学函数，得到我们想要计算的结果。
        #  我们将 sqrt{x}写成幂的形式 x^{1/2}，再使用自然对数 e 进行换底，即可得到：
        #       sqrt{x} = x^{1/2} = (e^{In x})^{1/2} = e^{1/2 * In x}
        #  这样我们就可以得到 sqrt{x}
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt2(self, x: int) -> int:
        # 二分法(时间复杂度：O(logx), 空间复杂度：O(1))
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

    def mySqrt3(self, x: int) -> int:
        # 牛顿迭代法(时间复杂度：O(logx), 空间复杂度：O(1))
        # 点A附近，切线与f(x)非常接近
        # 因为切线是一条直线（也就是线性的），所以我们可以说，A点的切线是f(x)的线性逼近。离A点距离越近，这种逼近的效果也就越好，
        # 也就是说，切线与曲线之间的误差越小。所以我们可以说在A点附近“ 切线≈f(x) ”。
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


if __name__ == '__main__':
    # case1  res = 2
    x1 = 4

    # case2  res = 2
    # 说明: 8 的平方根是 2.82842...,
    #      由于返回类型是整数，小数部分将被舍去。
    x2 = 8

    sol = Solution()
    res1 = sol.mySqrt1(x1), sol.mySqrt2(x1), sol.mySqrt3(x1)
    res2 = sol.mySqrt1(x2), sol.mySqrt2(x2), sol.mySqrt3(x2)
    print('case1:', res1)
    print('case2:', res2)