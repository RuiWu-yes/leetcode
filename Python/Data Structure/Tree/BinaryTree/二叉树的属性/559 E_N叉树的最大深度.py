# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 559 N 叉树的最大深度
# @Content : 给定一个 N 叉树，找到其最大深度。
#            最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#            N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth1(self, root: 'Node') -> int:
        # 递归法
        if not root: return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth1(root.children[i]))
        return depth + 1

    def maxDepth2(self, root: 'Node') -> int:
        # 迭代法
        # 层序遍历
        if not root: return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth