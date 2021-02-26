# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 25 K 个一组翻转链表
# @Content : 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。k 是一个正整数，它的值小于或等于链表的长度。
#            如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# @explain : 你的算法只能使用常数的额外空间。
#            你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        if not head: return
        # 区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for _ in range(k):
            # 不足 k 个，不需要反转，base case
            if not b: return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self, a, b):
        # 反转区间 [a, b) 的元素，注意是左闭右开
        pre, cur = None, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre


if __name__ == '__main__':
    from libs import linked_list as ll

    # 输入：1->2->3->4->5->NULL
    head = ListNode(1)
    sll = ll.SingleLinkedList(head)
    for x in [2, 3, 4, 5]: sll.append(x)

    # # case1  k = 2  输出：2->1->4->3->5->NULL
    # k = 2

    # case2  k = 3  输出：3->2->1->4->5->NULL
    k = 3

    sol = Solution()
    head1 = sol.reverseKGroup(head, k)

    for i in range(5):
        print('k = {}：'.format(k), head1.val, end=' ') if i == 0 else print(head1.val, end=' ')
        head1 = head1.next