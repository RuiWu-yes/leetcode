# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 2 两数相加
# @Content : 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#            请你将两个数相加，并以相同形式返回一个表示和的链表。
#            你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 直白写法
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode()
        s = 0  # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # p.next 指向新链表, 用来创建一个新的链表
            p = p.next  # p 向后遍历
            s //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 深度优先
        def dfs(node1, node2, carry):
            # node1: l1当前节点  node2: l2当前节点  carry: 进位(0或者1)
            if not node1 and not node2 and not carry: return
            s = (node1.val if node1 else 0) + (node2.val if node2 else 0) + carry
            node = ListNode(s % 10)
            node.next = dfs(node1.next if node1 else None, node2.next if node2 else None, s // 10)
            return node

        return dfs(l1, l2, 0)


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  res = [7, 0, 8]
    # 解释：342 + 465 = 807
    # l1 = [2,4,3], l2 = [5,6,4]
    l1_1, l2_1 = ListNode(2), ListNode(5)
    sll1_1 = ll.SingleLinkedList(l1_1)
    sll2_1 = ll.SingleLinkedList(l2_1)
    for x1 in [4, 3]: sll1_1.append(x1)
    for x2 in [6, 4]: sll2_1.append(x2)

    # case2  res = [0]
    # l1 = [0], l2 = [0]
    l1_2, l2_2 = ListNode(0), ListNode(0)

    # case3  res = [8, 9, 9, 9, 0, 0, 0, 1]
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    l1_3, l2_3 = ListNode(9), ListNode(9)
    sll1_3 = ll.SingleLinkedList(l1_3)
    sll2_3 = ll.SingleLinkedList(l2_3)
    for x1 in [9, 9, 9, 9, 9, 9]: sll1_1.append(x1)
    for x2 in [9, 9, 9]: sll1_1.append(x2)

    sol = Solution()
    res1 = sol.addTwoNumbers1(l1_1, l2_1), sol.addTwoNumbers2(l1_1, l2_1)
    res2 = sol.addTwoNumbers1(l1_2, l2_2), sol.addTwoNumbers2(l1_2, l2_2)
    res3 = sol.addTwoNumbers1(l1_3, l2_3), sol.addTwoNumbers2(l1_3, l2_3)
    print('case1:', res1[0].val)
    print('case2:', res2[0].val)
    print('case3:', res3[0].val)
