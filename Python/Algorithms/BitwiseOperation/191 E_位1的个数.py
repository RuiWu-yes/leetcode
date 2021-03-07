# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 191 位1的个数
# @Content : 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
#      提示 : 1) 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
#            因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
#            2) 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#      进阶 : 如果多次调用这个函数，你将如何优化你的算法？


class Solution:
    def hammingWeight(self, n: int) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 3
    # 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
    n1 = 11

    # case2  res = 1
    # 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
    n2 = 128

    # case3  res = 31
    # 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
    n3 = 4294967293

    sol = Solution()
    res1 = sol.hammingWeight(n1)
    res2 = sol.hammingWeight(n2)
    res3 = sol.hammingWeight(n3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)