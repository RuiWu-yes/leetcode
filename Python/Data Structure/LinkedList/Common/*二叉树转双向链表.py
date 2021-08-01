# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 剑指offer 二叉树转双向链表
# @Content : 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
#            比如输入下图中二叉搜索树，则输出转换后的排序双向链表


class BiTNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pHead = None  # 双向链表头结点
        self.pEnd = None  # 双向链表尾结点

    def arraytotree(self, array, start, end):
        # 把有序数组转换成二叉搜索树
        if end >= start:
            root = BiTNode()
            mid = (start + end + 1) // 2
            # 树的根节点为数组中间的元素
            root.val = array[mid]
            # 递归的用左半部分数组构造root的左子树
            root.left = self.arraytotree(array, start, mid - 1)
            # 递归用右半部分数组构造root的右子树
            root.right = self.arraytotree(array, mid + 1, end)
        else:
            root = None
        return root

    def inOrderBSTree(self, root):
        # 把二叉树转换成双向链表
        # 思路：由于转换后的双向链表中结点的顺序与二叉树的中序遍历相同，因此，可以对二叉树的中序遍历算法进行修改，
        #      通过在中序遍历的过程中修改结点的指向来转换成一个排序的双向链表。
        if not root: return

        self.inOrderBSTree(root.left)  # 转换root的左子树
        # 使当前结点的左子树指向双向链表中的最后一个结点
        root.left = self.pEnd
        # 双向链表为空，当前遍历的结点为双向链表的头结点
        if not self.pEnd:
            self.pHead = root
        else:
            self.pEnd.right = root
        self.pEnd = root
        self.inOrderBSTree(root.right)


if __name__ == '__main__':
    # case1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sol = Solution()
    root1 = sol.arraytotree(arr1, 0, len(arr1) - 1)
    sol.inOrderBSTree(root1)
    print("转化后双向链表正向遍历：")
    cur = sol.pHead
    while cur:
        print(cur.val, end=' ')
        cur = cur.right
    print(' ')
    print("转化后双向链表逆向遍历：")
    cur = sol.pEnd
    while cur:
        print(cur.val, end=' ')
        cur = cur.left