# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 212 单词搜索 II
# @Content : 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#            单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个
#            单元格内的字母在一个单词中不允许被重复使用。
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


if __name__ == '__main__':
    # case1  res = ["eat", "oath"]
    board1 = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]

    # case2  res = []
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]

    sol = Solution()
    res1 = sol.findWords(board1, words1)
    res2 = sol.findWords(board2, words2)
    print('case1:', res1)
    print('case2:', res2)