# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 208 实现 Trie (前缀树)
# @Content : 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#      说明： 1) 你可以假设所有的输入都是由小写字母 a-z 构成的。
#            2) 保证所有输入均为非空字符串。


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        初始化字典树的数据结构
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        插入单词到字典树中
        """
        tree = self.lookup
        for s in word:
            if s not in tree:
                tree[s] = {}  # 当前层
            tree = tree[s]  # 当前层的下一层
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        搜索单词是否在字典树中
        """
        tree = self.lookup
        for s in word:
            if s not in tree:
                return False
            tree = tree[s]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        字典树是否以给出的前缀(prefix)开头
        """
        tree = self.lookup
        for s in prefix:
            if s not in tree:
                return False
            tree = tree[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    # case1  res = true
    res1 = trie.search("apple")

    # case2  res = false
    res2 = trie.search("app")

    # case3  res = true
    res3 = trie.startsWith("app")

    # case4  res = true
    trie.insert("app")
    res4 = trie.search("app")

    print('case1', res1)
    print('case2', res2)
    print('case3', res3)
    print('case4', res4)