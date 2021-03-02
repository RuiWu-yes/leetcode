# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 226 翻转二叉树
# @Content : 翻转一棵二叉树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        ## -------------------------------------------
        # 递归法（前序遍历）
        if not root: return root
        root.left, root.right = root.right, root.left  # 根(交换左右子树)
        self.invertTree(root.left)                     # 左
        self.invertTree(root.right)                    # 右
        return root
        ## -------------------------------------------
        # 递归法（中序遍历）
        # if not root: return root
        # self.invertTree(root.left)                     # 左
        # root.left, root.right = root.right, root.left  # 根(交换左右子树)
        # # 注意：这里的 root.left 就是交换之前的 root.right
        # self.invertTree(root.left)                     # 右
        # return root
        ## -------------------------------------------
        # 递归法（后序遍历）
        # if not root: return root
        # self.invertTree(root.left)                     # 左
        # self.invertTree(root.right)                    # 右
        # root.left, root.right = root.right, root.left  # 根(交换左右子树)
        # return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        # 迭代法（层序遍历）
        if not root: return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left or node.right:
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = [4, 7, 2, 9, 6, 3, 1]
    # 输入：
    #      4
    #    /   \
    #   2     7
    #  / \   / \
    # 1   3 6   9
    # 输出：
    #      4
    #    /   \
    #   7     2
    #  / \   / \
    # 9   6 3   1
    list1 = [4, 2, 7, 1, 3, 6, 9]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    node1 = sol.invertTree(root1)
    node2 = sol.invertTree1(root1)

    from libs.tree import BinaryTree as BT
    res1_1, res1_2 = BT().inorder(node1), BT().inorder(node2)
    print('case1:', res1_1, res1_2)