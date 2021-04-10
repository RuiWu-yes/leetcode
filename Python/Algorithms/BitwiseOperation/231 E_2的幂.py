# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 231 2的幂
# @Content : 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pass


if __name__ == '__main__':
    # case1  res = true
    # 解释: 2^0 = 1
    n1 = 1

    # case2  res = true
    # 解释: 2^4 = 16
    n2 = 16

    # case3  res = false
    n3= 218

    sol = Solution()
    res1 = sol.isPowerOfTwo(n1)
    res2 = sol.isPowerOfTwo(n2)
    res3 = sol.isPowerOfTwo(n3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)