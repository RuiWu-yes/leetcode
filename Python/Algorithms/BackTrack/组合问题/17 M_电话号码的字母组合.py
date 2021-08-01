# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 17 电话号码的字母组合
# @Content : 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#            给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


phoneMap = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

class Solution:
    def letterCombinations(self, digits: str):
        # 回溯算法
        res = []
        if not digits: return res
        def backtrack(i, track):
            if len(track) == len(digits):
                res.append(''.join(track[:]))
                return
            if i > len(digits) - 1:
                return
            for s in phoneMap[digits[i]]:
                track.append(s)
                backtrack(i+1, track)
                track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1  res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    digits1 = "23"

    # case2  res = []
    digits2 = ""

    # case3  res = ["a", "b", "c"]
    digits3 = "2"

    sol = Solution()
    res1 = sol.letterCombinations(digits1)
    res2 = sol.letterCombinations(digits2)
    res3 = sol.letterCombinations(digits3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)