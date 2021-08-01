# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 530 二叉搜索树的最小绝对差
# @Content : 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#            * 二叉搜索树上求什么最值啊，差值之类的，就把它想成在一个有序数组上求最值，求差值，这样就简单多了
#            * 那么二叉搜索树采用中序遍历，其实就是一个有序数组


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference1(self, root: TreeNode) -> int:
        # 递归法
        # 中序遍历
        res = float('inf')
        pre = None  # pre作用是记录上一层的节点
        def traversal(cur):
            nonlocal res, pre
            if not cur: return
            traversal(cur.left)   # 左
            if pre:               # 根
                res = min(res, cur.val - pre.val)  # 当前节点cur与上一个节点pre比较绝对值之差
            pre = cur  # 上一步比较完之后，pre记录当前节点
            traversal(cur.right)  # 右
        traversal(root)
        return res

    def getMinimumDifference2(self, root: TreeNode) -> int:
        # 迭代法
        # 中序遍历
        stack = []
        res = float('inf')
        pre, cur = None, root
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left     # 左
            else:
                cur = stack.pop()
                if pre:            # 根
                    res = min(res, cur.val - pre.val)  # 当前节点cur与上一个节点pre比较绝对值之差
                pre = cur  # 上一步比较完之后，pre记录当前节点
                cur = cur.right    # 右
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = 1
    # 解释：最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
    #    1
    #     \
    #      3
    #     /
    #    2
    list1 = [1, None, 3, None, None, 2, None]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1_1, res1_2 = sol.getMinimumDifference1(root1), sol.getMinimumDifference2(root1)
    print('case1:', res1_1, res1_2)