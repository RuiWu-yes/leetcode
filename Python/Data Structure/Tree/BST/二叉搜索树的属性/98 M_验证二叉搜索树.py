# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 98 验证二叉搜索树
# @Content : 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# @explain : 假设一个二叉搜索树具有如下特征：
#               节点的左子树只包含小于当前节点的数。
#               节点的右子树只包含大于当前节点的数。
#               所有左子树和右子树自身必须也是二叉搜索树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 首先，对于每一个节点 root，它的左右孩子节点是否符合左小右大的原则
    # 其次，root 的整个左子树都要小于 root.val，整个右子树都要大于 root.val
    def isValidBST(self, root: TreeNode) -> bool:
        # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
        def isvalidBST(root, min, max):
            # base case
            if not root: return True
            # 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
            if min != None and root.val <= min.val: return False
            if max != None and root.val >= max.val: return False
            # 限定左子树的最大值是 root.val, 右子树的最小值是 root.val
            return isvalidBST(root.left, min, root) and isvalidBST(root.right, root, max)
        return isvalidBST(root, None, None)


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = true
    # 输入：
    #     2
    #    / \
    #   1   3
    list1 = [2, 1, 3]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = false
    # 输入:
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    # 解释: 输入为: [5,1,4,null,null,3,6]
    #      根节点的值为 5 ，但是其右子节点值为 4
    list2 = [5, 1, 4, None, None, 3, 6]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1 = sol.isValidBST(root1)
    res2 = sol.isValidBST(root2)
    print('case1: ', res1)
    print('case2: ', res2)