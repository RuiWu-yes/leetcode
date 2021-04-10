# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 433 最小基因变化
# @Content : 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#            假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#            例如，基因序列由 "AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#            与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#            现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需
#            的最少变化次数。如果无法实现目标变化，请返回 -1。
# @Att     : 1) 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
#            2) 如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
#            3) 假定起始基因序列与目标基因序列是不一样的。
from typing import List


class Solution:
    def minMutation1(self, start: str, end: str, bank: List[str]) -> int:
        # 单向BFS
        # ------------------------------------------------------------------
        # 第一种写法
        bank = set(bank)
        if end not in bank: return -1
        count = 0
        deque = [start]
        visited = {start}
        chars = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        while deque:
            for _ in range(len(deque)):
                cur = deque.pop(0)
                if cur == end: return count
                for i in range(len(cur)):
                    for s in chars[cur[i]]:
                        new_gene = cur[:i] + s + cur[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            deque.append(new_gene)
            count += 1  # 同一层遍历结束再+1, 同一层存的都是一次基因变化的结果
        return -1
        # ------------------------------------------------------------------
        # 第二种写法
        # bank = set(bank)
        # if end not in bank: return -1
        # deque = [[start, 0]]
        # visited = {start}
        # chars = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        # while deque:
        #     for _ in range(len(deque)):
        #         cur, count = deque.pop(0)
        #         if cur == end: return count
        #         for i in range(len(cur)):
        #             for s in chars[cur[i]]:
        #                 new_gene = cur[:i] + s + cur[i+1:]
        #                 if new_gene in bank and new_gene not in visited:
        #                     visited.add(new_gene)
        #                     deque.append([new_gene, count+1])
        # return -1

    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        # 双向BFS
        bank = set(bank)
        if end not in bank: return -1
        count = 0
        fore, back = {start}, {end}
        chars = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while fore:
            if len(fore) > len(back):  # 如果前方向和后方向长度不同，取短的那个方向进行BFS，可以遍历更少节点，更快的两方向相遇返回结果
                fore, back = back, fore
            count += 1  # 遍历一层，就计数+1
            temp = set()  # 临时temp存下一层节点
            for cur in fore:
                for i in range(len(cur)):
                    for s in chars[cur[i]]:
                        new_gene = cur[:i] + s + cur[i+1:]
                        if new_gene in back:
                            return count  # 表示双向BFS相遇了，返回最终结果
                        if new_gene in bank:
                            temp.add(new_gene)
                            bank.remove(new_gene)  # 做减法查重效率比做加法更高效
            fore = temp  # 此时的temp层是相对于fore的下一层
        return -1


if __name__ == '__main__':
    # case1  res = 1
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]

    # case2  res = 2
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

    # case3  res = 3
    start3 = "AAAAACCC"
    end3 = "AACCCCCC"
    bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

    sol = Solution()
    res1 = sol.minMutation1(start1, end1, bank1), sol.minMutation2(start1, end1, bank1)
    res2 = sol.minMutation1(start2, end2, bank2), sol.minMutation2(start2, end2, bank2)
    res3 = sol.minMutation1(start3, end3, bank3), sol.minMutation2(start3, end3, bank3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)