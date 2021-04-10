# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 127 单词接龙
# @Content : 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：
#               1) 序列中第一个单词是 beginWord 。
#               2) 序列中最后一个单词是 endWord 。
#               3) 每次转换只能改变一个字母。
#               4) 转换过程中的中间单词必须是字典 wordList 中的单词。
#            给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。
#            如果不存在这样的转换序列，返回 0。
from typing import List


class Solution:
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 单向BFS
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        count = 1
        deque = [beginWord]
        while deque:
            for _ in range(len(deque)):
                word = deque.pop(0)
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for s in "qwertyuiopasdfghjklzxcvbnm":
                        if s == word[i]: continue
                        newWord = word[:i] + s + word[i+1:]
                        if newWord in wordSet:
                            deque.append(newWord)
                            wordSet.remove(newWord)
            count += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 双向BFS
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        count = 1
        fore, back = {beginWord}, {endWord}
        while fore and back:
            if len(fore) > len(back):  # 如果前方向和后方向长度不同，取短的那个方向进行BFS，可以遍历更少节点，更快的两方向相遇返回结果
                fore, back = back, fore
            count += 1  # 遍历一层，就计数+1
            temp = set()  # 临时temp存下一层节点
            for word in fore:
                for i in range(len(word)):
                    for s in "qwertyuiopasdfghjklzxcvbnm":
                        if s == word[i]: continue
                        newWord = word[:i] + s + word[i+1:]
                        if newWord in back:
                            return count  # 表示双向BFS相遇了，返回最终结果
                        if newWord in wordSet:
                            temp.add(newWord)
                            wordSet.remove(newWord)
            fore = temp  # 此时的temp层是相对于fore的下一层
        return 0


if __name__ == '__main__':
    # case1  res = 5
    # 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]

    # case2  res = 0
    # 解释：endWord "cog" 不在字典中，所以无法进行转换。
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]

    sol = Solution()
    res1 = sol.ladderLength1(beginWord1, endWord1, wordList1), sol.ladderLength2(beginWord1, endWord1, wordList1)
    res2 = sol.ladderLength1(beginWord2, endWord2, wordList2), sol.ladderLength2(beginWord2, endWord2, wordList2)
    print('case1:', res1)
    print('case2:', res2)