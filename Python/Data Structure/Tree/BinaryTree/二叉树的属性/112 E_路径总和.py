# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 112 路径总和
# @Content : 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，
#            这条路径上所有节点值相加等于目标和 targetSum 。
#            叶子节点 是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum1(self, root: TreeNode, targetSum: int) -> bool:
        # 递归法
        if not root: return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        Left = self.hasPathSum1(root.left, targetSum - root.val)
        Right= self.hasPathSum1(root.right, targetSum - root.val)
        return Left | Right

    def hasPathSum2(self, root: TreeNode, targetSum: int) -> bool:
        # 迭代法
        if not root: return False
        stack = [[root, root.val]]
        while stack:
            node = stack.pop()
            # 如果该节点是叶子节点了,同时该节点的路径数值等于sum,那么就返回true
            if not node[0].left and not node[0].right and targetSum == node[1]:
                return True
            # 右节点,压进去一个节点的时候,将该节点的路径数值也记录下来
            if node[0].right:
                stack.append([node[0].right, node[1] + node[0].right.val])
            # 左节点, 压进去一个节点的时候, 将该节点的路径数值也记录下来
            if node[0].left:
                stack.append([node[0].left, node[1] + node[0].left.val])
        return False


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = true
    list1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root1 = Tree.lct(None, list1, 0)
    targetSum1 = 22

    # case2  res = false
    list2 = [1, 2, 3]
    root2 = Tree.lct(None, list2, 0)
    targetSum2 = 5

    # case3  res = false
    list3 = [1, 2]
    root3 = Tree.lct(None, list3, 0)
    targetSum3 = 0

    sol = Solution()
    res1_1, res1_2 = sol.hasPathSum1(root1, targetSum1), sol.hasPathSum2(root1, targetSum1)
    res2_1, res2_2 = sol.hasPathSum1(root2, targetSum2), sol.hasPathSum2(root2, targetSum2)
    res3_1, res3_2 = sol.hasPathSum1(root3, targetSum3), sol.hasPathSum2(root3, targetSum3)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)
    print('case3:', res3_1, res3_2)