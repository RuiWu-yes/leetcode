# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 557 反转字符串中的单词 III
# @Content : 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#      提示 : 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution:
    def reverseWords1(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

    def reverseWords2(self, s: str) -> str:
        # 利用栈(先入后出)
        s = s + " "
        stack, res = [], ""
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res = res + stack.pop()
        return res[1:]


if __name__ == '__main__':
    # case1  res = "s'teL ekat edoCteeL tsetnoc"
    s1 = "Let's take LeetCode contest"

    sol = Solution()
    res1 = sol.reverseWords1(s1), sol.reverseWords2(s1)
    print('case1:', res1)