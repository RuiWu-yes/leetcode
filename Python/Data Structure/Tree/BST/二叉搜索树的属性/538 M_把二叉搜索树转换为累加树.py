# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 538 把二叉搜索树转换为累加树
# @Content : 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
#            使每个节点 node的新值等于原树中大于或等于node.val的值之和。
# @Att     : 提醒一下，二叉搜索树满足下列约束条件：
#               节点的左子树仅包含键 小于 节点键的节点。
#               节点的右子树仅包含键 大于 节点键的节点。
#               左右子树也必须是二叉搜索树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 反序中序遍历(右根左)
        sum = 0
        def traverse(root):
            # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
            nonlocal sum
            if not root: return
            traverse(root.right)  # 右
            # 维护累加和            # 根
            sum += root.val
            # 将BST转化成累加树
            root.val = sum
            traverse(root.left)   # 左
        traverse(root)
        return root


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree
    from libs.tree import BinaryTree

    # case1  res = [30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]
    Tree = ListCreateTree()
    list = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root = Tree.lct(None, list, 0)

    sol = Solution()
    result = sol.convertBST(root)
    res = BinaryTree().inorder(result)
    print(res)