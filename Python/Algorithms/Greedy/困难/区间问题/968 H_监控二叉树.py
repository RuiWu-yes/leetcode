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
        pass


if __name__ == '__main__':
    # case1  res = 1
    # 解释：如图所示，一台摄像头足以监控所有节点。
    list1 = [0, 0, None, 0, 0]

    # case2  res = 2
    # 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
    list2 = [0, 0, None, 0, None, 0, None, None, 0]