# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 114 二叉树展开为链表
# @Content : 给定一个二叉树，原地将它展开为一个单链表。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root: return

        self.flatten(root.left)   # 左
        self.flatten(root.right)  # 右
        # 后序遍历位置
        # 1.左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2.将左子树作为右子树
        root.left = None
        root.right = left
        # 3.将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    def traverse(root):
        res = []
        while root:
            if not root: return
            res.append(root.val)
            root = root.right
        return res

    # 例如，给定二叉树
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    Tree = ListCreateTree()
    list = [1, 2, 5, 3, 4, None, 6]
    root = Tree.lct(None, list, 0)
    # 将其展开为：
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6
    sol = Solution()
    sol.flatten(root)
    res = traverse(root)
    print(res)