# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 66 加一
# @Content : 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#            最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#            你可以假设除了整数 0 之外，这个整数不会以零开头。
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 情况一：数组中末尾不为9，直接末尾+=1
        # 情况二：数组中末尾为9，遍历从低位到高位，只要碰到9就变成0，当碰到第一个不为9的数就+=1然后return
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == '__main__':
    # case1  res = [1, 2, 4]
    # 解释：输入数组表示数字 123。
    digits1 = [1, 2, 3]

    # case2  res = [4, 3, 2, 2]
    # 解释：输入数组表示数字 4321。
    digits2 = [4, 3, 2, 1]

    # case3  res = [1]
    digits3 = [0]

    sol = Solution()
    res1 = sol.plusOne(digits1)
    res2 = sol.plusOne(digits2)
    res3 = sol.plusOne(digits3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)