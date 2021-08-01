# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 513 找树左下角的值
# @Content : 给定一个二叉树，在树的最后一行找到最左边的值。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 迭代法
        # 层序遍历
        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if i == 0:
                    res = node.val  # 记录当前行的第一个元素
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 1
    #     2
    #    / \
    #   1   3
    list1 = [2, 1, 3]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = 7
    #         1
    #        / \
    #       2   3
    #      /   / \
    #     4   5   6
    #        /
    #       7
    list2 = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, None]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1 = sol.findBottomLeftValue(root1)
    res2 = sol.findBottomLeftValue(root2)
    print('case1:', res1)
    print('case2:', res2)