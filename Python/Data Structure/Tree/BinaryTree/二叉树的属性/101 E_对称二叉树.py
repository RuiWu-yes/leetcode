# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 101 对称二叉树
# @Content : 给定一个二叉树，检查它是否是镜像对称的。
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 正是因为要遍历两棵树而且要比较内侧和外侧节点，所以准确的来说是一个树的遍历顺序是左右根，一个树的遍历顺序是右左根
    # 后序也可以理解为是一种回溯
    def isSymmetric1(self, root: TreeNode) -> bool:
        # 递归法
        if not root: return True
        def compare(left, right):
            if not left and right: return False
            elif left and not right: return False
            elif not left and not right: return True
            elif left.val != right.val: return False
            else:
                return compare(left.left, right.right) and compare(left.right, right.left)
        return compare(root.left, root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        # 迭代法(使用队列)
        if not root: return True
        queue = collections.deque([root.left, root.right])
        while queue:  # 接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:  # 左节点为空、右节点为空，此时说明是对称的
                continue
            # 左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)    # 加入左节点左孩子
            queue.append(rightNode.right)  # 加入右节点右孩子
            queue.append(leftNode.right)   # 加入左节点右孩子
            queue.append(rightNode.left)   # 加入右节点左孩子
        return True

    def isSymmetric3(self, root: TreeNode) -> bool:
        # 迭代法(使用栈)
        if not root: return True
        stack = [root.left, root.right]
        while stack:
            leftNode = stack.pop()
            rightNode = stack.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            stack.append(leftNode.left)  # 加入左节点左孩子
            stack.append(rightNode.right)  # 加入右节点右孩子
            stack.append(leftNode.right)  # 加入左节点右孩子
            stack.append(rightNode.left)  # 加入右节点左孩子
        return True


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = true
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    list1 = [1, 2, 2, 3, 4, 4, 3]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = false
    #     1
    #    / \
    #   2   2
    #    \   \
    #    3    3
    list2 = [1, 2, 2, None, 3, None, 3]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1_1, res1_2, res1_3 = sol.isSymmetric1(root1), sol.isSymmetric2(root1), sol.isSymmetric3(root1)
    res2_1, res2_2, res2_3 = sol.isSymmetric1(root2), sol.isSymmetric2(root2), sol.isSymmetric3(root2)
    print('case1:', res1_1, res1_2, res1_3)
    print('case2:', res2_1, res2_2, res2_3)