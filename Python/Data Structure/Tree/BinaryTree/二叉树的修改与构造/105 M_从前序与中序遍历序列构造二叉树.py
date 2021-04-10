# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 105 从前序与中序遍历序列构造二叉树
# @Content : 根据一棵树的前序遍历与中序遍历构造二叉树。
# @Att     : 你可以假设树中没有重复的元素。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        return self.build(preorder, 0, len(preorder)-1,
                          inorder, 0, len(inorder)-1)

    def build(self, preorder, preStart, preEnd,
              inorder, inStart, inEnd):
        # base case
        if preStart > preEnd: return

        # root节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        # rootVal在中序遍历数组中的索引
        index = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break
        # 左子树的节点个数
        leftSize = index - inStart
        # 递归构造左右子树
        root.left = self.build(preorder, preStart+1, preStart+leftSize,
                               inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd,
                                inorder, index+1, inEnd)
        return root


if __name__ == '__main__':
    from libs.tree import BinaryTree

    # case1
    # 输入
    preorder = [3, 9, 20, 15, 7]  # 前序遍历
    inorder = [9, 3, 15, 20, 7]   # 中序遍历
    # 输出  返回如下的二叉树：
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    res = BinaryTree().inorder(root)
    print(res)