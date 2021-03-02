# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 222 完全二叉树的节点个数
# @Content : 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#            完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
#            并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1 ~ 2h 个节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 普通二叉树的逻辑来求 ------------------------------------------------------
    def countNodes1(self, root: TreeNode) -> int:
        # 递归法
        if not root: return 0
        return self.countNodes1(root.left) + self.countNodes1(root.right) + 1

    def countNodes2(self, root: TreeNode) -> int:
        # 迭代法
        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop()
                res += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res

    # 完全二叉树的逻辑来求 ------------------------------------------------------
    # 完全二叉树只有两种情况，情况一:就是满二叉树，情况二:最后一层叶子节点没有满。
    #    对于情况一，可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。
    #    对于情况二，分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，然后依然可以 按照情况1来计算。
    def countNodes3(self, root: TreeNode) -> int:
        # 递归法
        if not root: return 0
        left = root.left
        right = root.right
        leftHeight = rightHeight = 0  # 这里初始为0是有目的的，为了下面求指数方便
        while left:  # 求左子树深度
            left = left.left
            leftHeight += 1
        while right:  # 求右子树深度
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return (2 << leftHeight) - 1  # 注意(2<<1) 相当于2^2，所以leftHeight初始为0
        return self.countNodes3(root.left) + self.countNodes3(root.right) + 1


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 6
    list1 = [1, 2, 3, 4, 5, 6]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1_1, res1_2, res1_3 = sol.countNodes1(root1), sol.countNodes2(root1), sol.countNodes3(root1)
    print('case1:', res1_1, res1_2, res1_3)