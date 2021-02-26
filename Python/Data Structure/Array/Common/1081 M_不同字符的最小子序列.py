# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1081 不同字符的最小子序列 == 316 去除重复字母(解法一样)
# @Content : 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
from collections import Counter, defaultdict


class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
    res1 = sol.smallestSubsequence(s1)
    res2 = sol.smallestSubsequence(s2)
    print('case1:', res1)
    print('case2:', res2)