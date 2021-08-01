# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 完全二叉树最后一个节点(类似于leetcode 222 完全二叉树的节点个数)
# @Content : 给定一棵完全二叉树，返回最后一层的最右边的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getlastNode(self, root: TreeNode):
        # 思路：递归，
        #      求子树的高度：如果左子树高度 > 右子树高度，则在左子树继续递归过程；
        #      否则在右子树继续递归。如果当前节点为叶子节点，则返回；
        #      由于是完全二叉树，求高度时只需一直往左遍历即可。每次递归都下降一层，每次都求树的高度
        #      时间复杂度为O(lgN * lgN)。
        if not root or not root.left:
            return root
        leftHeight = rightHeight = 0  # 左子树高度
        left, right = root.left, root.right
        while left:
            left = left.left
            leftHeight += 1
        while right:
            right = right.left  # 从左孩子开始计算高度
            rightHeight += 1

        if leftHeight > rightHeight:
            return self.getlastNode(root.left)
        else:  # 相等时也是在右子树递归
            return self.getlastNode(root.right)


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 6
    list1 = [1, 2, 3, 4, 5, 6]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1 = sol.getlastNode(root1)
    print('case1:', res1.val)