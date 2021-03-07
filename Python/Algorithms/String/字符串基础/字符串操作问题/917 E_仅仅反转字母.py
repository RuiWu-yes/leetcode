# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 917 仅仅反转字母
# @Content : 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。


class Solution:
    def reverseOnlyLetters1(self, S: str) -> str:
        # 双指针
        ls = list(S)
        left, right = 0, len(ls) - 1
        while left < right:
            if not ls[left].isalpha():
                left += 1
            elif not ls[right].isalpha():
                right -= 1
            else:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
        return "".join(ls)

    def reverseOnlyLetters2(self, S: str) -> str:
        # 字母栈
        letters = [c for c in S if c.isalpha()]
        res = []
        for c in S:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        return "".join(res)


if __name__ == '__main__':
    # case1  res = "dc-ba"
    s1 = "ab-cd"

    # case2  res = "j-Ih-gfE-dCba"
    s2 = "a-bC-dEf-ghIj"

    # case3  res = "Qedo1ct-eeLg=ntse-T!"
    s3 = "Test1ng-Leet=code-Q!"

    sol = Solution()
    res1 = sol.reverseOnlyLetters1(s1), sol.reverseOnlyLetters2(s1)
    res2 = sol.reverseOnlyLetters1(s2), sol.reverseOnlyLetters2(s2)
    res3 = sol.reverseOnlyLetters1(s3), sol.reverseOnlyLetters2(s3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)