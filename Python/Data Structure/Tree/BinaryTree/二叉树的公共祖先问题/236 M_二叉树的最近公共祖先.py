# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 236 二叉树的最近公共祖先
# @Content : 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#            百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
#            最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深
#            度尽可能大（一个节点也可以是它自己的祖先）。”


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # 递归法
        # base case
        if not root: return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)    # 左
        right = self.lowestCommonAncestor(root.right, p, q)  # 右
        # 情况一: 如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）
        if left and right: return root
        # 情况二: 如果 p 和 q 都不在以 root 为根的树中，直接返回 None
        if not left and not right: return
        # 情况三: 如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点
        return left if left else right


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # case1  res = 3
    # 	      3
    # 	    /   \
    # 	   5     1
    # 	  / \   / \
    # 	 6   2 0   8
    #       / \
    #      7   4
    list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    Tree = ListCreateTree()
    root = Tree.lct(None, list, 0)
    p1 = root.left   # p1 = 5
    q1 = root.right  # q1 = 1
    # case2  res = 5
    p2 = p1                    # p2 = 5
    q2 = root.left.right.left  # q2 = 7

    sol = Solution()
    res1 = sol.lowestCommonAncestor(root, p1, q1)
    print('case1:', res1.val)
    res2 = sol.lowestCommonAncestor(root, p2, q2)
    print('case2:', res2.val)