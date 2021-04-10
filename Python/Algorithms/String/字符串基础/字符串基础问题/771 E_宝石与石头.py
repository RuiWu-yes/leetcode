# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 771 宝石与石头
# @Content : 给定字符串 J 代表石头中宝石的类型，和字符串 S 代表你拥有的石头。S 中每个字符代表了一种你拥有的石头的类型，
#            你想知道你拥有的石头中有多少是宝石。
#            J中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。


class Solution:
    def numJewelsInStones1(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        return sum([stones.count(x) for x in jewels])


if __name__ == '__main__':
    # case1  res = 3
    J1 = "aA"
    S1 = "aAAbbbb"

    # case2  res = 0
    J2 = "z"
    S2 = "ZZ"

    sol = Solution()
    res1 = sol.numJewelsInStones1(J1, S1), sol.numJewelsInStones2(J1, S1)
    res2 = sol.numJewelsInStones1(J2, S2), sol.numJewelsInStones2(J2, S2)
    print('case1:', res1)
    print('case2:', res2)