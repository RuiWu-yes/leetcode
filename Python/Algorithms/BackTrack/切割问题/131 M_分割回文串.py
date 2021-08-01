# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 131 分割回文串
# @Content : 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#            返回 s 所有可能的分割方案。


class Solution:
    def partition(self, s: str):
        # 回溯算法
        res = []
        def backtrack(start, track):
            if start >= len(s):
                res.append(track[:])
                return
            for end in range(start+1, len(s)+1):  # end表示的是s[start:end], end是开区间取不到
                str = s[start:end]
                if str == str[::-1]:  # 判断是否为回文串
                    track.append(str)
                    backtrack(end, track)
                    track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1  res = [["aa", "b"], ["a", "a", "b"]]
    s = "aab"

    sol = Solution()
    res1 = sol.partition(s)
    print('case1:', res1)