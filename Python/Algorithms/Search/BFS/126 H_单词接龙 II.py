# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 126 单词接龙 II
# @Content : 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
#            1.每次转换只能改变一个字母。
#            2.转换后得到的单词必须是字典中的单词。
# @Explain : 1) 如果不存在这样的转换序列，返回一个空列表。
#            2) 所有单词具有相同的长度。
#            3) 所有单词只由小写字母组成。
#            4) 字典中不存在重复的单词。
#            5) 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
from typing import List
from collections import defaultdict


class Solution:
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 单向BFS
        res = []
        wordSet = set(wordList)
        if endWord not in wordSet: return res

        dic = defaultdict(list)
        for w in wordSet:
            for i in range(len(wordList[0])):
                dic[w[:i] + '*' + w[i+1:]].append(w)

        queue, queue1 = [(beginWord, [beginWord])], []
        visited = set()
        while queue:
            for _ in range(len(queue)):
                word, path = queue.pop()
                visited.add(word)
                if word == endWord: res.append(path)
                for i in range(len(word)):
                    for newWord in dic[word[:i] + '*' + word[i+1:]]:
                        if newWord not in visited:
                            queue1.append((newWord, path + [newWord]))
            if res: return res  # 广度优先搜索，只要res第一次添加，即添加的是最短转换序列
            queue, queue1 = queue1, queue
        return res

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 双向BFS
        wordSet = set(wordList)
        if endWord not in wordSet: return []
        fore, back, flag = {beginWord}, {endWord}, True  # flag的作用是记录fore还是back方向(True代表fore方向，False代表back方向)
        dic = defaultdict(set)  # 记录变换一次的路径
        while fore:
            if len(fore) > len(back):  # 如果前方向和后方向长度不同，取短的那个方向进行BFS，可以遍历更少节点，更快的两方向相遇返回结果
                fore, back, flag = back, fore, not flag
            wordSet -= fore  # 做减法查重
            temp = set()  # 临时temp存下一层节点
            for word in fore:
                for i in range(len(word)):
                    for s in 'abcdefghijklmnopqrstuvwxyz':
                        if s == word[i]: continue
                        newWord = word[:i] + s + word[i+1:]
                        if newWord in wordSet:
                            temp.add(newWord)
                            if flag:
                                dic[newWord].add(word)
                            else:
                                dic[word].add(newWord)
            if temp & back:  # 求两个集合的交集，返回的也是集合(有交集说明fore和back相遇了，可以返回结果了)
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[x]+i for i in res for x in dic[i[0]]]
                return res
            fore = temp
        return []


if __name__ == '__main__':
    # case1  res = [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]

    # case2  res = []
    # 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]

    # case3  res = [["a","c"]]
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]

    sol = Solution()
    res1 = sol.findLadders1(beginWord1, endWord1, wordList1), sol.findLadders2(beginWord1, endWord1, wordList1)
    res2 = sol.findLadders1(beginWord2, endWord2, wordList2), sol.findLadders2(beginWord2, endWord2, wordList2)
    res3 = sol.findLadders1(beginWord3, endWord3, wordList3), sol.findLadders2(beginWord3, endWord3, wordList3)
    print('case1:', res1[0], ' | ', res1[1])
    print('case2:', res2)
    print('case3:', res3)