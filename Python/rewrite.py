from typing import List
from collections import Counter, defaultdict


class Solution:
    # 要求一、要去重。
    # 要求二、去重字符串中的字符顺序不能打乱 s 中字符出现的相对顺序。
    # 要求三、在所有符合上一条要求的去重字符串中，字典序最小的作为最终结果。
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack, instack = [], defaultdict(lambda: False)
        for c in s:
            count[c] -= 1
            if instack[c]: continue
            while stack and stack[-1] > c:
                if count[stack[-1]] == 0: break
                instack[stack.pop()] = False
            stack.append(c)
            instack[c] = True
        return ''.join(stack)


if __name__ == '__main__':
    # case1  res = "abc"
    s1 = "bcabc"

    # case2  res = "acdb"
    s2 = "cbacdcbc"