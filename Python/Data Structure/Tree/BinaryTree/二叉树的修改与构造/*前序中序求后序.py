# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 从前序与中序遍历序列求后序遍历
# @Content : 根据一棵树的前序遍历与中序遍历求得这个二叉树的后序遍历
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> List:
        return self.build(preorder, 0, len(preorder)-1,
                          inorder, 0, len(inorder)-1)

    def build(self, preorder, preStart, preEnd,
              inorder, inStart, inEnd):
        res = []
        # base case
        if preStart > preEnd: return res

        # root节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # rootVal在中序遍历数组中的索引
        index = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break
        # 左子树的节点个数
        leftSize = index - inStart
        # 递归右左子树
        right = self.build(preorder, preStart+leftSize+1, preEnd,
                                inorder, index+1, inEnd)
        left = self.build(preorder, preStart+1, preStart+leftSize,
                               inorder, inStart, index-1)
        res.extend(left)
        res.extend(right)
        res.append(rootVal)

        return res


if __name__ == '__main__':
    # case1  res = [9, 15, 7, 20, 3]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    preorder1 = [3, 9, 20, 15, 7]  # 前序遍历
    inorder1 = [9, 3, 15, 20, 7]   # 中序遍历

    # case2  res = [1, 3, 2, 5, 7, 6, 4]
    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
    preorder2 = [4, 2, 1, 3, 6, 5, 7]  # 前序遍历
    inorder2 = [1, 2, 3, 4, 5, 6, 7]   # 中序遍历

    sol = Solution()
    res1 = sol.buildTree(preorder1, inorder1)
    res2 = sol.buildTree(preorder2, inorder2)
    print('case1:', res1)
    print('case2:', res2)
