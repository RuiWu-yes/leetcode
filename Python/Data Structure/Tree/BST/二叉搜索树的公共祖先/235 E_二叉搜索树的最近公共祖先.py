# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 235 二叉搜索树的最近公共祖先
# @Content : 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#            百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
#            满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#            例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归法
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 迭代法
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 6
    # 解释: 节点 2 和节点 8 的最近公共祖先是 6。
    list1 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root1 = Tree.lct(None, list1, 0)
    p1 = TreeNode(2)
    q1 = TreeNode(8)

    # case2  res = 2
    # 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
    list2 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root2 = Tree.lct(None, list2, 0)
    p2 = TreeNode(2)
    q2 = TreeNode(4)

    sol = Solution()
    node1_0, node1_1 = sol.lowestCommonAncestor(root1, p1, q1), sol.lowestCommonAncestor1(root1, p1, q1)
    node2_0, node2_1 = sol.lowestCommonAncestor(root2, p2, q2), sol.lowestCommonAncestor1(root2, p2, q2)
    print('case1:', node1_0.val, node1_1.val)
    print('case2:', node2_0.val, node2_1.val)