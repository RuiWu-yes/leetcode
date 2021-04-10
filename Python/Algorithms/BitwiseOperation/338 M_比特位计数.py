# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 338 比特位计数
# @Content : 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#      进阶 : 1) 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
#            2) 要求算法的空间复杂度为O(n)。
#            3) 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
from typing import List


class Solution:
    def countBits1(self, num: int) -> List[int]:
        # 动态规划 + 位运算 (最高有效位)
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits

    def countBits2(self, num: int) -> List[int]:
        # 动态规划 + 位运算 (最低有效位)
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

    def countBits3(self, num: int) -> List[int]:
        # 动态规划 + 位运算 (最低设置位)
        # 定义正整数 x 的「最低设置位」为 x 的二进制表示中的最低的 1 所在位。例如，1010 的二进制表示是 1010(2)
        # 其最低设置位为 2，对应的二进制表示是 10(2)
        # 令 y=x&(x−1)，则 y 为将 x 的最低设置位从 1 变成 0 之后的数，显然 0≤y<x，bits[x]=bits[y]+1。
        # 因此对任意正整数 x，都有 bits[x]=bits[x&(x−1)]+1。
        # 遍历从 1 到 num 的每个正整数 ii，计算 bits 的值。最终得到的数组 bits 即为答案。
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits


if __name__ == '__main__':
    # case1  res = [0, 1, 1]
    num1 = 2

    # case2  res = [0, 1, 1, 2, 1, 2]
    num2 = 5

    sol = Solution()
    res1 = sol.countBits1(num1), sol.countBits2(num1), sol.countBits3(num1)
    res2 = sol.countBits1(num2), sol.countBits2(num2), sol.countBits3(num2)
    print('case1:', res1)
    print('case2:', res2)