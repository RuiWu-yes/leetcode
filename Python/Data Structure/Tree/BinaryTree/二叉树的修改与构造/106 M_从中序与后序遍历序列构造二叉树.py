# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 106 从中序与后序遍历序列构造二叉树
# @Content : 根据一棵树的中序遍历与后序遍历构造二叉树。
# @Att     : 你可以假设树中没有重复的元素。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        return self.build(inorder, 0, len(inorder)-1,
                          postorder, 0, len(postorder)-1)

    def build(self, inorder, inStart, inEnd,
              postorder, postStart, postEnd):
        # base case
        if inStart > inEnd: return

        # root节点对应的值就是后序遍历数组的最后一个元素
        rootVal = postorder[postEnd]
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
        root.left = self.build(inorder, inStart, index-1,
                               postorder, postStart, postStart+leftSize-1)
        root.right = self.build(inorder, index+1, inEnd,
                                postorder, postStart+leftSize, postEnd-1)
        return root

    def travesed(self, root):
        res = []
        deque = [root]
        while deque:
            node = deque.pop(0)
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res


if __name__ == '__main__':
    from libs.tree import BinaryTree

    # case1
    # 输入
    inorder = [9, 3, 15, 20, 7]  # 中序遍历
    postorder = [9, 15, 7, 20, 3]  # 后序遍历
    # 返回如下的二叉树：
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    sol = Solution()
    root = sol.buildTree(inorder, postorder)
    res = BinaryTree().inorder(root)
    print(res)
