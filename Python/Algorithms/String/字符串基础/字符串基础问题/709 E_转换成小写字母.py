# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 709 转换成小写字母
# @Content : 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。


class Solution:
    def toLowerCase1(self, str: str) -> str:
        return ''.join([chr(ord(s) + 32) if 65 <= ord(s) <= 90 else s for s in str])

    def toLowerCase2(self, str: str) -> str:
        ls = list(str)
        for i in range(len(ls)):
            if 65 <= ord(ls[i]) <= 90:
                ls[i] = chr(ord(ls[i]) + 32)
        return "".join(ls)


if __name__ == '__main__':
    # case1  res = "hello"
    str1 = "Hello"

    # case2  res = "here"
    str2 = "here"

    # case3  res = "lovely"
    str3 = "LOVELY"

    sol = Solution()
    res1 = sol.toLowerCase1(str1), sol.toLowerCase2(str1)
    res2 = sol.toLowerCase1(str2), sol.toLowerCase2(str2)
    res3 = sol.toLowerCase1(str3), sol.toLowerCase2(str3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)