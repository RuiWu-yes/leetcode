# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 669 修剪二叉搜索树
# @Content : 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
#            修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
#            所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 递归法
        if not root: return
        if root.val < low: return self.trimBST(root.right, low, high)
        if root.val > high: return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

    def trimBST1(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 迭代法
        pass
    #     # 因为二叉搜索树的有序性,不需要使用栈模拟递归的过程。
    #     if not root: return
    #     # 处理头结点,让root移动到[low, high] 范围内,注意是左闭右闭
    #     while root.val < low or root.val > high:
    #         if root.val < low:  # 小于low往右走
    #             root = root.right
    #         else:               # 大于high往左走
    #             root = root.left
    #     cur = root
    #     # 此时root已经在[low, high] 范围内,处理左孩子元素小于low的情况
    #     while cur:
    #         while cur.left and cur.left.val < low:
    #             cur.left = cur.left.right
    #         cur = cur.left
    #     cur = root
    #     # 此时root已经在[low, high] 范围内,处理右孩子大于high的情况
    #     while cur:
    #         while cur.right and cur.right.val > high:
    #             cur.right = cur.right.left
    #         cur = cur.right
    #     return root


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = [1, None, 2]
    list1 = [1, 0, 2]
    root1 = Tree.lct(None, list1, 0)
    low1 = 1
    high1 = 2

    # case2  res = [3, 2, None, 1]
    list2 = [3, 0, 4, None, 2, None, None, None, None, 1]
    root2 = Tree.lct(None, list2, 0)
    low2 = 1
    high2 = 3

    # case3  res = [1]
    list3 = [3]
    root3 = Tree.lct(None, list3, 0)
    low3 = 2
    high3 = 2

    # case4  res = [1, None, 2]
    list4 = [1, None, 2]
    root4 = Tree.lct(None, list4, 0)
    low4 = 1
    high4 = 3

    # case5  res = [2]
    list5 = [1, None, 2]
    root5 = Tree.lct(None, list5, 0)
    low5 = 2
    high5 = 4

    sol = Solution()
    node1_0, node1_1 = sol.trimBST(root1, low1, high1), sol.trimBST1(root1, low1, high1)
    node2_0, node2_1 = sol.trimBST(root2, low2, high2), sol.trimBST1(root2, low2, high2)
    node3_0, node3_1 = sol.trimBST(root3, low3, high3), sol.trimBST1(root3, low3, high3)
    node4_0, node4_1 = sol.trimBST(root4, low4, high4), sol.trimBST1(root4, low4, high4)
    node5_0, node5_1 = sol.trimBST(root5, low5, high5), sol.trimBST1(root5, low5, high5)

    from libs.tree import BinaryTree as BT
    print('case1:', BT().inorder(node1_0), BT().inorder(node1_1))
    print('case2:', BT().inorder(node2_0), BT().inorder(node2_1))
    print('case3:', BT().inorder(node3_0), BT().inorder(node3_1))
    print('case4:', BT().inorder(node4_0), BT().inorder(node4_1))
    print('case5:', BT().inorder(node5_0), BT().inorder(node5_1))