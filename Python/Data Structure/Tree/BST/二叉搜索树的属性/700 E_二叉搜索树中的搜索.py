# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 700 二叉搜索树中的搜索
# @Content : 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。
#            如果节点不存在，则返回 NULL。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if not root: return
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # 给定二叉搜索树:
    #         4
    #        / \
    #       2   7
    #      / \
    #     1   3
    list = [4, 2, 7, 1, 3]
    Tree = ListCreateTree()
    root = Tree.lct(None, list, 0)
    val = 2
    # 返回
    #       2
    #      / \
    #     1   3
    sol = Solution()
    res = sol.searchBST(root, val)
    print(res.val, res.left.val, res.right.val)