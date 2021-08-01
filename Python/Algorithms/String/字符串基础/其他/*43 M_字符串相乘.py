# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 43 字符串相乘
# @Content : 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 对于比较小的数字，做运算可以直接使用编程语言提供的运算符，但是如果相乘的两个因数非常大，语言提供的数据类型可能就会溢出。
        # 一种替代方案就是，运算数以字符串的形式输入，然后模仿我们小学学习的乘法算术过程计算出结果，并且也用字符串表示。
        # 需要注意的是，num1 和 num2 可以非常长，所以不可以把他们直接转成整型然后运算，唯一的思路就是模仿我们手算乘法。
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        # 从个位数开始逐位相乘
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # 乘积在 res 对应的索引位置
                p1, p2 = i + j, i + j + 1
                # 叠加到 res 上
                sum = mul + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10  # 进位
        # 将计算结果转化成字符串
        string = ''
        for i in range(len(res)):
            if not string and res[i] == 0:  # 结果前缀可能存的 0（未使用的位）
                continue
            string += str(res[i])
        return string if string else '0'


if __name__ == '__main__':
    # case1  res = "0"
    num1_1 = "0"
    num1_2 = "0"

    # case2  res = "6"
    num2_1 = "2"
    num2_2 = "3"

    # case3  res = "56088"
    num3_1 = "123"
    num3_2 = "456"

    sol = Solution()
    res1 = sol.multiply(num1_1, num1_2)
    res2 = sol.multiply(num2_1, num2_2)
    res3 = sol.multiply(num3_1, num3_2)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)