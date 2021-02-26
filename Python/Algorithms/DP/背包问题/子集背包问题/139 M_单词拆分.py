# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 139 单词拆分
# @Content : 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
#            判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# @Explain : 拆分时可以重复使用字典中的单词。
#            你可以假设字典中没有重复的单词。
import functools


class Solution:
    def wordBreak1(self, s: str, wordDict) -> bool:
        # 动态规划
        # 背包问题
        # dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True  # 初始化 dp[0] = True，空字符可以被表示。
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

    def wordBreak2(self, s: str, wordDict) -> bool:
        # 记忆化回溯
        # functools.lru_cache的作用主要是用来做缓存，他能把相对耗时的函数结果进行保存，避免传入相同的参数重复计算。
        # 同时，缓存并不会无限增长，不用的缓存会被释放。
        @functools.lru_cache(None)
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res
        return back_track(s)


if __name__ == '__main__':
    # case1  res = true
    # 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]

    # case2  res = true
    # 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。注意你可以重复使用字典中的单词。
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]

    # case3  res = false
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]

    sol = Solution()
    res1_1, res1_2 = sol.wordBreak1(s1, wordDict1), sol.wordBreak2(s1, wordDict1)
    res2_1, res2_2 = sol.wordBreak1(s2, wordDict2), sol.wordBreak2(s2, wordDict2)
    res3_1, res3_2 = sol.wordBreak1(s3, wordDict3), sol.wordBreak2(s3, wordDict3)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)
    print('case3:', res3_1, res3_2)