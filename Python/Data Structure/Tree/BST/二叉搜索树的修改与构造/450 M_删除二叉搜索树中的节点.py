# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 450 删除二叉搜索树中的节点
# @Content : 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。
#            返回二叉搜索树（有可能被更新）的根节点的引用。
# @Explain   一般来说，删除节点可分为两个步骤：
#                1.首先找到需要删除的节点；
#                2.如果找到了，删除它。
#            说明： 要求算法时间复杂度为 O(h)，h 为树的高度。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        if not root: return
        if root.val == key:
            # 把两个 if 把情况 1 和 2 都正确处理了
            if not root.left: return root.right
            if not root.right: return root.left
            # 处理情况 3
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node):
        # BST 最左边就是最小的
        while node.left:
            node = node.left
        return node


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # case1
    #     5
    #    / \
    #   3   6
    #  / \   \
    # 2   4   7
    list = [5, 3, 6, 2, 4, None, 7]
    Tree = ListCreateTree()
    root = Tree.lct(None, list, 0)
    key = 3
    # 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
    # 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示:
    #     5
    #    / \
    #   4   6
    #  /     \
    # 2       7
    # 另一个正确答案是 [5,2,6,null,4,null,7]。
    #     5
    #    / \
    #   2   6
    #    \   \
    #     4   7
    sol = Solution()
    res = sol.deleteNode(root, key)