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
        # 前缀树 + DFS
        # * 本题的前提是了解Trie。通过words里面的单词，来构建Trie，也就是说Trie代表了所有单词。然后通过DFS，一边遍历board，一边同时来看Trie。
        # 相当于一个边走边对照的过程。一旦走到某一步发现，board里上下左右的字母，都不在我同时正在走的这条Trie的路的下一个备选字母之中，便终止此路，
        # 这条路前面和board相同的字母，也都没有意义。
        # * 优化主要体现在Trie，要一边找一边修改Trie。如何修改？
        #      上面说Trie的某条路走不下去了便终止，但一旦能走下去并且走到头，完整地找到words的某个单词，那就把Trie里面这个单词删掉，
        #      以免后面board出现相似或者相同项，重走老路，因为确实已经找到这个单词了，无需再让这个找到的单词存在于Trie里了。
        #      这个优化的想法，体现在last = tree[s].pop('finish', False)和 if not tree[s]: tree.pop(s)这两个位置。
        res = []
        row, col = len(board), len(board[0])  # m, n 分别代表行、列
        # 构建字典树
        Tree = {}  # 整颗字典树
        for word in words:
            tree = Tree  # 此树代表当前层下的树
            for s in word:
                if s not in tree:
                    tree[s] = {}
                tree = tree[s]
            tree['finish'] = word

        def dfs(r, c, tree):
            s = board[r][c]
            # 优化点：一旦能走下去并且走到头，完整地找到words的某个单词，那就把Trie里面这个单词删掉，以免后面board出现相似或者相同项，重走老路
            last = tree[s].pop('finish', False)  # 字典pop(key, default): key值必须给出. 否则, 返回default值
            if last:
                res.append(last)
            # 比如case3这种情况, 如果没有以下这步，那么对于[["a", "a"]]， 在i,j为0,1的时候，会重复看左边，然后又递归i,j为0,0的情况，
            # 这样'aaa', 就被加入到结果中。
            board[r][c] = '#'  # 相当于已经拜访过
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # “相邻”单元格是那些水平相邻或垂直相邻的单元格(即左右上下)
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] in tree[s]:
                    dfs(nr, nc, tree[s])
            # 恢复board[r][c]的原始值
            board[r][c] = s
            # 优化点：一旦能走下去并且走到头，完整地找到words的某个单词，那就把Trie里面这个单词删掉，以免后面board出现相似或者相同项，重走老路
            if not tree[s]:  # 字典为空则删掉此键值
                tree.pop(s)

        for i in range(row):
            for j in range(col):
                if board[i][j] in Tree:
                    dfs(i, j, Tree)
        return res


if __name__ == '__main__':
    # case1  res = ["eat", "oath"]
    # 前缀树: {'o': {'a': {'t': {'h': {'finish': 'oath'}}}},
    #         'p': {'e': {'a': {'finish': 'pea'}}},
    #         'e': {'a': {'t': {'finish': 'eat'}}},
    #         'r': {'a': {'i': {'n': {'finish': 'rain'}}}}}
    board1 = [["o", "a", "a", "n"],
              ["e", "t", "a", "e"],
              ["i", "h", "k", "r"],
              ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]

    # case2  res = []
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]

    # case3  res = []
    board3 = [["a", "a"]]
    words3 = ["aaa"]

    sol = Solution()
    res1 = sol.findWords(board1, words1)
    res2 = sol.findWords(board2, words2)
    res3 = sol.findWords(board3, words3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)