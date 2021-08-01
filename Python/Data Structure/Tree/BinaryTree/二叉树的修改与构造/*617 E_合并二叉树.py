# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 617 合并二叉树
# @Content : 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#            你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为
#            节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        ## -----------------------------------------------------------------------------
        # 递归法（前序遍历）
        if not root1: return root2  # 如果root1为空,合并之后就应该是root2
        if not root2: return root1  # 如果root2为空,合并之后就应该是root1
        root1.val += root2.val                                   # 根
        root1.left = self.mergeTrees(root1.left, root2.left)     # 左
        root1.right = self.mergeTrees(root1.right, root2.right)  # 右
        return root1
        ## -----------------------------------------------------------------------------
        # 递归法（中序遍历）
        # if not root1: return root2  # 如果root1为空,合并之后就应该是root2
        # if not root2: return root1  # 如果root2为空,合并之后就应该是root1
        # root1.left = self.mergeTrees(root1.left, root2.left)     # 左
        # root1.val += root2.val                                   # 根
        # root1.right = self.mergeTrees(root1.right, root2.right)  # 右
        # return root1
        ## -----------------------------------------------------------------------------
        # 递归法（后序遍历）
        # if not root1: return root2  # 如果root1为空,合并之后就应该是root2
        # if not root2: return root1  # 如果root2为空,合并之后就应该是root1
        # root1.left = self.mergeTrees(root1.left, root2.left)     # 左
        # root1.right = self.mergeTrees(root1.right, root2.right)  # 右
        # root1.val += root2.val                                   # 根
        # return root1

    def mergeTrees1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 迭代法(层序遍历)
        if not root1: return root2
        if not root2: return root1
        queue = [[root1, root2]]
        while queue:
            node1, node2 = queue.pop(0)
            # 此时两个节点一定不为空,val相加
            node1.val += node2.val
            # 如果两棵树左节点都不为空,加入队列
            if node1.left and node2.left:
                queue.append([node1.left, node2.left])
            # 如果两棵树右节点都不为空,加入队列
            if node1.right and node2.right:
                queue.append([node1.right, node2.right])
            # 当root1的左节点为空, root2左节点不为空, 就赋值过去
            if not node1.left and node2.left:
                node1.left = node2.left
            # 当root1的右节点为空, root2右节点不为空, 就赋值过去
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = [3, 4, 5, 5, 4, 7]
    # 	     Tree 1                    Tree 2
    #           1                         2
    #          / \                       / \
    #         3   2                     1   3
    #        /                           \   \
    #       5                             4   7
    # 合并后的树:
    # 	     3
    # 	    / \
    # 	   4   5
    # 	  / \   \
    # 	 5   4   7

    list1 = [1, 3, 2, 5, None]
    list2 = [2, 1, 3, None, 4, None, 7]
    root1 = Tree.lct(None, list1, 0)
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    # node1_1 = sol.mergeTrees(root1, root2)
    node1_2 = sol.mergeTrees1(root1, root2)

    from libs.tree import BinaryTree as BT
    # res1_1 = BT().inorder(node1_1)
    res1_2 = BT().inorder(node1_2)
    # print('case1:', res1_1)
    print('case1:', res1_2)