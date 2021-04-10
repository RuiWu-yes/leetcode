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
        # 这个问题稍微复杂，跟插入操作类似，先「找」再「改」
        # 找到目标节点了，比方说是节点 A，如何删除这个节点，这是难点。因为删除节点的同时不能破坏 BST 的性质。有三种情况。
        #    情况 1：A 恰好是叶子节点，两个子节点都为空，那么它可以当场去世了。
        #    情况 2：A 只有一个非空子节点，那么它要让这个孩子接替自己的位置。
        #    情况 3：A 有两个子节点，麻烦了，为了不破坏 BST 的性质，A 必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。
        if not root: return
        if root.val == key:
            # 用两个 if 把情况 1 和 2 都正确处理了
            if not root.left: return root.right
            if not root.right: return root.left
            # 处理情况 3 (方式一:右子树中最小的那个节点来接替自己)
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
            # 处理情况 3 (方式二:左子树中最大的那个节点来接替自己)
            # maxNode = self.getMax(root.left)
            # root.val = maxNode.val
            # root.left = self.deleteNode(root.left, maxNode.val)
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

    def getMax(self, node):
        # BST 最右边就是最大的
        while node.right:
            node = node.right
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
    node = sol.deleteNode(root, key)

    from libs.tree import BinaryTree as BT
    print('case1:', BT().inorder(node))