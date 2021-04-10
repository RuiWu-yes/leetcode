# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 20 有效的括号
# @Content : 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#            有效字符串需满足：
#               1) 左括号必须用相同类型的右括号闭合。
#               2) 左括号必须以正确的顺序闭合。


class Solution:
    def isValid(self, s: str) -> bool:
        # 栈(先入后出)
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in dic:
                stack.append(c)
            elif not stack or dic[c] != stack.pop():
                return False
        return not stack


if __name__ == '__main__':
    # case1  res = true
    s1 = "()"

    # case2  res = true
    s2 = "()[]{}"

    # case3  res = false
    s3 = "(]"

    # case4  res = false
    s4 = "([)]"

    # case5  res = true
    s5 = "{[]}"

    sol = Solution()
    res1 = sol.isValid(s1)
    res2 = sol.isValid(s2)
    res3 = sol.isValid(s3)
    res4 = sol.isValid(s4)
    res5 = sol.isValid(s5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)