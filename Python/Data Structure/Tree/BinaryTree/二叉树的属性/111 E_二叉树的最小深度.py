# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 111 二叉树的最小深度
# @Content : 给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# @Explain : 叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        # 递归法
        if not root: return 0
        if not root.left and root.right:  # 左节点为空，右节点不为空
            return self.minDepth1(root.right) + 1
        if root.left and not root.right:  # 左节点不为空，右节点为空
            return self.minDepth1(root.left) + 1
        return min(self.minDepth1(root.left), self.minDepth1(root.right)) + 1  # 左节点不为空，右节点不为空

    def minDepth2(self, root: TreeNode) -> int:
        # 迭代法
        # 层序遍历: 当某一层出现无左右孩子的节点时，此层的深度即为最小深度
        if not root: return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1  # 记录最小深度
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:  # 当左右孩子都为空的时候，说明是最低点的一层了，退出
                    return depth
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 2
    list1 = [3, 9, 20, None, None, 15, 7]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = 5
    list2 = [2, None, 3, None, 4, None, 5, None, 6]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1_1, res1_2 = sol.minDepth1(root1), sol.minDepth2(root1)
    res2_1, res2_2 = sol.minDepth1(root2), sol.minDepth2(root2)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)