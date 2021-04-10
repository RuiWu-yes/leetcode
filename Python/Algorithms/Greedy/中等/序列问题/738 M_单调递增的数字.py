# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 738 单调递增的数字
# @Content : 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
#           （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 贪心算法
        # 局部最优:遇到strList[i - 1] > strList[i]的情况，让strList[i - 1]--，
        #         然后strList[i]给为9，可以保证这两位 变成最大单调递增整数。
        # 全局最优:得到小于等于N的最大单调递增的整数。
        # 但这里局部最优推出全局最优，还需要其他条件，即遍历顺序，和标记从哪一位开始统一改成9。
        strList = list(str(N))
        # flag用来标记赋值9从哪里开始
        # 设置为这个默认值，为了防止第二个for循环在flag没有被赋值的情况下执行
        flag = len(strList)
        for i in range(len(strList)-1, 0, -1):
            if strList[i-1] > strList[i]:
                flag = i
                strList[i-1] = str(int(strList[i-1]) - 1)
        for i in range(flag, len(strList)):
            strList[i] = '9'
        return int(''.join(strList))


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