# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 652 寻找重复的子树
# @Content : 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#            两棵树重复是指它们具有相同的结构以及相同的结点值。
#            因此，你需要以列表的形式返回上述重复子树的根结点。
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        # 后序遍历(左右根)
        res = []
        memo = defaultdict(lambda: 0)
        def traverse(root):
            if not root: return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subtree = left + ',' + right + ',' + str(root.val)
            freq = memo[subtree]
            if freq == 1:
                res.append(root)
            memo[subtree] += 1
            return subtree
        traverse(root)
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # 示例 1：
    #         1
    #        / \
    #       2   3
    #      /   / \
    #     4   2   4
    #        /
    #       4

    # 下面是两个重复的子树：
    #       2   和   4
    #      /
    #     4
    Tree = ListCreateTree()
    list = [1, 2, 3, 4, None, 2, 4, None, None, None, None, 4]
    root = Tree.lct(None, list, 0)

    sol = Solution()
    res = sol.findDuplicateSubtrees(root)
    print([[res[0].val], [res[1].val, res[1].left.val]])