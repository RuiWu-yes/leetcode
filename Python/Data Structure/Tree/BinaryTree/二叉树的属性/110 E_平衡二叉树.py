# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 110 平衡二叉树
# @Content : 给定一个二叉树，判断它是否是高度平衡的二叉树。
#            本题中，一棵高度平衡二叉树定义为：
#            一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 递归法
        def getDepth(node):
            if not node: return 0
            leftDepth = getDepth(node.left)
            if leftDepth == -1: return -1  # 说明左子树已经不是二叉平衡树
            rightDepth = getDepth(node.right)
            if rightDepth == -1: return -1  # 说明右子树已经不是二叉平衡树
            return -1 if abs(leftDepth - rightDepth) > 1 else 1 + max(leftDepth, rightDepth)
        return False if getDepth(root) == -1 else True


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = true
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1 = sol.isBalanced(root1)
    print('case1:', res1)