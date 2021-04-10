# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 205 同构字符串
# @Content : 给定两个字符串 s 和 t，判断它们是否是同构的。
#            如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#            每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，
#            相同字符只能映射到同一个字符上，字符可以映射到自己本身。


class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        # zip
        # zip(a, b, c, ...)函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
        # 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        word = zip(*set(zip(s, t)))
        for w in word:
            if len(w) != len(set(w)):
                return False
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        # map
        return [*map(s.index, s)] == [*map(t.index, t)]

    def isIsomorphic3(self, s: str, t: str) -> bool:
        # index
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

    def isIsomorphic4(self, s: str, t: str) -> bool:
        # 哈希表
        dic1 = dict()
        dic2 = dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
                return False
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        return True

    def isIsomorphic5(self, s: str, t: str) -> bool:
        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))


if __name__ == '__main__':
    # case1  res = true
    s1 = "egg"
    t1 = "add"

    # case2  res = false
    s2 = "foo"
    t2 = "bar"

    # case3  res = true
    s3 = "paper"
    t3 = "title"

    sol = Solution()
    res1 = sol.isIsomorphic1(s1, t1), sol.isIsomorphic2(s1, t1), sol.isIsomorphic3(s1, t1), sol.isIsomorphic4(s1, t1), sol.isIsomorphic5(s1, t1)
    res2 = sol.isIsomorphic1(s2, t2), sol.isIsomorphic2(s2, t2), sol.isIsomorphic3(s2, t2), sol.isIsomorphic4(s2, t2), sol.isIsomorphic5(s2, t2)
    res3 = sol.isIsomorphic1(s3, t3), sol.isIsomorphic2(s3, t3), sol.isIsomorphic3(s3, t3), sol.isIsomorphic4(s3, t3), sol.isIsomorphic5(s3, t3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)