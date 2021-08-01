# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 404 左叶子之和
# @Content : 计算给定二叉树的所有左叶子之和。
#            如果左节点不为空,且左节点没有左右孩子,那么这个节点就是左叶子


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves1(self, root: TreeNode) -> int:
        # 递归法
        if not root: return 0
        leftValue = self.sumOfLeftLeaves1(root.left)  # 左
        rightValue = self.sumOfLeftLeaves1(root.right)  # 右
        midValue = 0
        if root.left and not root.left.left and not root.left.right:  # 找到左叶子节点的值
            midValue = root.left.val
        return midValue + leftValue + rightValue

    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        # 迭代法(使用栈去模拟递归)
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:  # 找到左叶子节点的值
                res += node.left.val
            if node.right:  # 右
                stack.append(node.right)
            if node.left:  # 左
                stack.append(node.left)
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 24
    # 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1_1, res1_2 = sol.sumOfLeftLeaves1(root1), sol.sumOfLeftLeaves2(root1)
    print('case1:', res1_1, res1_2)