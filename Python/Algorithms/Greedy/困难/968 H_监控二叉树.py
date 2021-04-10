# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 968 监控二叉树
# @Content : 给定一个二叉树，我们在树的节点上安装摄像头。
#            节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
#            计算监控树的所有节点所需的最小摄像头数量。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 贪心算法
        # 局部最优：让叶子节点的父节点安摄像头，所用摄像头最少
        # 整体最优：全部摄像头数量所用最少！
        res = 0
        def traversal(cur):
            nonlocal res
            if not cur: return 2
            left = traversal(cur.left)  # 左
            right = traversal(cur.right)  # 右
            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                res += 1
                return 1
            else:
                return 2
        if traversal(root) == 0:  # root 无覆盖
            res += 1
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # case1  res = 1
    #         o
    #        /
    #       o
    #      / \
    #     o   o
    # 解释：如图所示，一台摄像头足以监控所有节点。
    Tree = ListCreateTree()
    list1 = [0, 0, None, 0, 0]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = 2
    #         o
    #        /
    #       o
    #      /
    #     o
    #    /
    #   o
    #    \
    #     o
    # 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
    list2 = [0, 0, None, 0, None, 0, None, None, 0]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1 = sol.minCameraCover(root1)
    res2 = sol.minCameraCover(root2)
    print('case1:', res1)
    print('case2:', res2)