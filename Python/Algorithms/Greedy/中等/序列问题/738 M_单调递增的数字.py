# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 
# @Content : 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
#           （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 9
    N1 = 10

    # case2  res = 1234
    N2 = 1234

    # case3  res = 299
    N3 = 332

    sol = Solution()
    res1 = sol.monotoneIncreasingDigits(N1)
    res2 = sol.monotoneIncreasingDigits(N2)
    res3 = sol.monotoneIncreasingDigits(N3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)