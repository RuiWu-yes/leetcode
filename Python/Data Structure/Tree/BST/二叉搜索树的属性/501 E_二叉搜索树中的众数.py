# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 501 二叉搜索树中的众数
# @Content : 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#            假定 BST 有如下定义：
#                1) 结点左子树中所含结点的值小于等于当前结点的值
#                2) 结点右子树中所含结点的值大于等于当前结点的值
#                3) 左子树和右子树都是二叉搜索树
# @Att     : 如果众数超过1个，不需考虑输出顺序
#      进阶 ：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
        self.pre = None
        self.cur_count, self.res_count, self.max_count = 0, 0, 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        self.pre = None
        self.res = [0] * self.res_count
        self.cur_count = self.res_count = 0
        self.inOrder(root)
        return self.res

    def inOrder(self, root: TreeNode) -> None:
        # 中序遍历
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.res_count = 1
        elif self.cur_count == self.max_count:
            if self.res:
                self.res[self.res_count] = root.val
            self.res_count += 1
        self.pre = root
        self.inOrder(root.right)


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    Tree = ListCreateTree()
    # case1  res = [2]
    #    1
    #     \
    #      2
    #     /
    #    2
    list1 = [1, None, 2, None, None, 2]
    root1 = Tree.lct(None, list1, 0)

    sol = Solution()
    res1 = sol.findMode(root1)
    print('case1:', res1)