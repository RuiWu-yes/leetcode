# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 50 Pow(x, n)
# @Content : 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治算法(递归方式)
        #   若n为偶数：n//2个 x | n//2个 x
        #   若n为奇数：n//2个 x | n//2个 x | x
        if n == 0:  # n为0情况
            return 1
        if n < 0:   # n为负数情况
            return 1 / self.myPow(x, -n)
        if n % 2:   # n为奇数情况
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)  # n为偶数情况

    def myPow1(self, x: float, n: int) -> float:
        # 位运算
        if n < 0:  # n为负数情况
            x = 1 / x
            n = - n
        pow = 1
        while n:  # n为0时，直接返回pow=1；n不为0时，进入循环
            if n & 1:  # n为奇数
                pow *= x
            x *= x
            n >>= 1  # 相当于n /= 2
        return pow


if __name__ == '__main__':
    # case1  res = 1024.00000
    x1 = 2.00000
    n1 = 10

    # case2  res = 9.26100
    x2 = 2.10000
    n2 = 3

    # case3  res = 0.25000
    # 解释：2-2 = 1/22 = 1/4 = 0.25
    x3 = 2.00000
    n3 = -2

    sol = Solution()
    res1_0, res1_1 = sol.myPow(x1, n1), sol.myPow1(x1, n1)
    res2_0, res2_1 = sol.myPow(x2, n2), sol.myPow1(x2, n2)
    res3_0, res3_1 = sol.myPow(x3, n3), sol.myPow1(x3, n3)
    print('case1:', res1_0, res1_1)
    print('case2:', res2_0, res2_1)
    print('case3:', res3_0, res3_1)