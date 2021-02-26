# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 316 去除重复字母 == 1081 不同字符的最小子序列(解法一样)
# @Content : 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
#            需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
from collections import Counter, defaultdict


class Solution:
    # 要求一、要去重。
    # 要求二、去重字符串中的字符顺序不能打乱 s 中字符出现的相对顺序。
    # 要求三、在所有符合上一条要求的去重字符串中，字典序最小的作为最终结果。
    def removeDuplicateLetters(self, s: str) -> str:
        # 维护一个计数器记录字符串 s 中字符的数量
        count = Counter(s)
        # stack: [栈]存放去重的结果  instack: [字典]记录栈中是否存在某个字符
        stack, instack = [], defaultdict(lambda: 0)
        for c in s:
            count[c] -= 1  # 每遍历过一个字符，都将对应的计数减 1
            if instack[c]: continue  # 如果字符 c 存在栈中，直接跳过 ♥
            # 插入操作之前，和之前的元素比较一下大小, 如果字典序比前面的小，pop 前面的元素
            while stack and stack[-1] > c:
                if count[stack[-1]] == 0: break  # 若之后不存在栈顶元素了，则停止 pop ♥
                instack[stack.pop()] = False  # 弹出栈顶元素，并把该元素标记为不在栈中
            # 如果字符 c 不在栈中，则插入栈顶并标记为存在
            stack.append(c)
            instack[c] = True
        return ''.join(stack)


if __name__ == '__main__':
    # case1  res = "abc"
    s1 = "bcabc"

    # case2  res = "acdb"
    s2 = "cbacdcbc"

    sol = Solution()
    res1 = sol.removeDuplicateLetters(s1)
    res2 = sol.removeDuplicateLetters(s2)
    print('case1:', res1)
    print('case2:', res2)