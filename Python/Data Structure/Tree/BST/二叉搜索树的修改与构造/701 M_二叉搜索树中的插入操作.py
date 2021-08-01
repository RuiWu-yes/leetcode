# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 701 二叉搜索树中的插入操作
# @Content : 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
#            输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
# @Att     : 可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到空位置插入新节点
        if not root: return TreeNode(val)
        # if root.val == val: BST中一般不会插入已存在元素
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree
    from libs.tree import BinaryTree

    # case1  res = [4, 2, 7, 1, 3, 5]
    #     4               4
    #    / \            /   \
    #   2   7   -->    2     7
    #  / \            / \   /
    # 1   3          1   3 5
    list = [4, 2, 7, 1, 3]
    Tree = ListCreateTree()
    root = Tree.lct(None, list, 0)
    val = 5

    sol = Solution()
    node = sol.insertIntoBST(root, val)
    res = BinaryTree().inorder(node)
    print(res)