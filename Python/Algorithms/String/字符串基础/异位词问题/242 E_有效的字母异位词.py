# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 242 有效的字母异位词
# @Content : 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词（字母种类一样且相同字母的个数一样）。
#      说明： 你可以假设字符串只包含小写字母。
#      进阶： 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 排序
        ls1 = list(s)
        ls1.sort()
        s = "".join(ls1)

        ls2 = list(t)
        ls2.sort()
        t = "".join(ls2)
        return s == t

    def isAnagram1(self, s: str, t: str) -> bool:
        # 使用Python自带的计数器Counter(哈希表)
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        # 集合去重, 然后字符串计数
        if len(t) != len(s):
            return False
        c = set(t)
        for i in c:
            if t.count(i) != s.count(i):
                return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        # 哈希算法
        # 用一个字典对s中的字母进行计数, 再对t中的字母到字典中元素比对
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in t:
            if i not in dic:
                return False
            else:
                if dic[i] == 1:  # 当等于1的时候，如果不删除，则 -1 会等于 0，最后dic不会置空
                    del dic[i]
                else:
                    dic[i] -= 1
        return not dic


if __name__ == '__main__':
    # case1  res = true
    s1 = "anagram"
    t1 = "nagaram"

    # case2  res = false
    s2 = "rat"
    t2 = "car"

    sol = Solution()
    res1 = sol.isAnagram(s1, t1), sol.isAnagram1(s1, t1), sol.isAnagram2(s1, t1), sol.isAnagram3(s1, t1)
    res2 = sol.isAnagram(s2, t2), sol.isAnagram1(s2, t2), sol.isAnagram2(s2, t2), sol.isAnagram3(s2, t2)
    print('case1:', res1)
    print('case2:', res2)