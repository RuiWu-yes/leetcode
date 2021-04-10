# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 116 填充每个节点的下一个右侧节点指针
# @Content : 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#            struct Node {
#              int val;
#              Node *left;
#              Node *right;
#              Node *next;
#            }
#            填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#            初始状态下，所有 next 指针都被设置为 NULL。
#      进阶 ：你只能使用常量级额外空间。
#            使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 递归
        if not root: return root
        def connectTwoNode(node1, node2):
            if not node1 or not node2: return
            # 前序遍历
            # 将传入的两个节点连接
            node1.next = node2
            # 连接相同父节点的两个子节点
            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            # 连接跨越父节点的两个子节点
            connectTwoNode(node1.right, node2.left)
        connectTwoNode(root.left, root.right)
        return root

    def traverse(self, root):
        res = []
        deque = collections.deque([root])
        while deque:
            node = deque.popleft()
            res.append(node.val)
            if not node.next: res.append('#')
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res


if __name__ == '__main__':
    from libs.list2tree import ListCreateTree

    # case1  输出：[1, #, 2, 3, #, 4, 5, 6, 7, #]
    # 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，
    #      如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
    Tree = ListCreateTree(1)
    list = [1, 2, 3, 4, 5, 6, 7]
    root = Tree.lct(None, list, 0)

    sol = Solution()
    root = sol.connect(root)
    res = sol.traverse(root)
    print(res)