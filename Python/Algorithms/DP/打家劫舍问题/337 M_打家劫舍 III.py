# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 337 打家劫舍 III
# @Content : 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
#            除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列
#            类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。计算在不触动警报的情况下，小偷
#            一晚能够盗取的最高金额。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# The binary tree can be created by list.
class ListCreateTree():
    def lct(self, root, list, i):  # 用列表递归创建二叉树，
        # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
        # 再接着创建b的右子树，
        if i < len(list):
            if list[i] == None:
                return None  # 这里的return很重要
            else:
                root = TreeNode(list[i])
                # 往左递推
                root.left = self.lct(root.left, list, 2*i+1)  # 从根开始一直到最左，直至为空，
                # 往右回溯
                root.right = self.lct(root.right, list, 2*i+2)  # 再返回上一个根，回溯右，
                # 再返回根'
                return root  # 这里的return很重要
        return root

class Solution:
    def rob1(self, root: TreeNode) -> int:
        # 动态规划：带备忘录的递归解法
        if not root: return 0
        memo = {}
        if root in memo:
            return memo[root]
        # 抢，然后去下下家（root的左子树的下下家以及右子树的下下家）
        left = 0 if not root.left else self.rob1(root.left.left) + self.rob1(root.left.right)
        right = 0 if not root.right else self.rob1(root.right.left) + self.rob1(root.right.right)
        do_it = root.val + left + right
        # 不抢，然后去下家
        not_do = self.rob1(root.left) + self.rob1(root.right)
        res = max(do_it, not_do)
        memo[root] = res
        return res

    def rob2(self, root: TreeNode) -> int:
        # 分治递归
        def _rob(root):
            if not root: return 0, 0  # 偷，不偷
            left = _rob(root.left)
            right = _rob(root.right)
            # 偷当前节点, 则左右子树都不能偷
            do_it = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            not_do = max(left) + max(right)
            return do_it, not_do
        return max(_rob(root))


if __name__ == '__main__':
    Tree = ListCreateTree()

    # case1  res = 7
    # 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
    #      3
    #     / \
    #    2   3
    #     \   \
    #      3   1
    list1 = [3, 2, 3, None, 3, None, 1]
    root1 = Tree.lct(None, list1, 0)

    # case2  res = 9
    # 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
    #      3
    #     / \
    #    4   5
    #   / \   \
    #  1   3   1
    list2 = [3, 4, 5, 1, 3, None, 1]
    root2 = Tree.lct(None, list2, 0)

    sol = Solution()
    res1_1 = sol.rob1(root1)
    res1_2 = sol.rob2(root1)
    res2_1 = sol.rob1(root2)
    res2_2 = sol.rob2(root2)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)