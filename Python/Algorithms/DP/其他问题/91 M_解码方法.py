# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 91 解码方法
# @Content : 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#               'A' -> 1
#               'B' -> 2
#               ...
#               'Z' -> 26
#            要解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
#            例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）
#            映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。
#
#            给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
#            题目数据保证答案肯定是一个 32 位 的整数。


class Solution:
    def numDecodings(self, s: str) -> int:
        pass


if __name__ == '__main__':
    # case1  res = 2
    # 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
    s1 = "12"

    # case2  res = 3
    # 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
    s2 = "226"

    # case3  res = 0
    # 解释：没有字符映射到以 0 开头的数字。含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
    # 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
    s3 = "0"

    # case4  res = 0
    # 解释："06" 不能映射到 "F" ，因为字符串开头的 0 无法指向一个有效的字符。
    s4 = "06"

    sol = Solution()
    res1 = sol.numDecodings(s1)
    res2 = sol.numDecodings(s2)
    res3 = sol.numDecodings(s3)
    res4 = sol.numDecodings(s4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)