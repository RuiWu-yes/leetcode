# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 链表奇偶位升降序排序
# @Content : 一个单链表,奇数位是升序的,偶数位是降序的,要求给它进行排序


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def init_linkedlist(self, l):
        """创建不带头结点的单链表"""
        head = ListNode()
        tail = head
        for val in l:
            tail.next = ListNode(val)
            tail = tail.next
        tail.next = None
        return head.next

    def split_linkedlist(self, head):
        """按照奇偶位拆分为两个链表"""
        head1 = head2 = None
        cur1 = cur2 = None
        count = 1
        while head:
            if count % 2 == 1:
                if cur1:
                    cur1.next = head
                    cur1 = cur1.next
                else:
                    cur1 = head1 = head
            else:
                if cur2:
                    cur2.next = head
                    cur2 = cur2.next
                else:
                    cur2 = head2 = head
            head = head.next
            count += 1
        cur1.next = None
        cur2.next = None
        return head1, head2

    def reverse_linkedlist(self, head):
        """反转链表"""
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre

    def merge_linkedlist(self, head1, head2):
        """合并两个递增链表"""
        head = ListNode()  # 设置一个临时结点
        tail = head
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # 合并剩余结点
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return head.next

    def traverse(self, root):
        while root:
            print(root.val, end=' ')
            root = root.next


if __name__ == '__main__':
    S = Solution()
    head = S.init_linkedlist([1, 200, 10, 120, 30, 8, 88, 4])  # 创建一个不带头结点的单链表：1->8->2->7->3->6->4->5

    head1, head2 = S.split_linkedlist(head)  # 1.按照奇偶位拆分为两个链表
    head2 = S.reverse_linkedlist(head2)  # 2.反转偶数结点构成的链表
    head = S.merge_linkedlist(head1, head2)  # 3.合并两个递增链表

    S.traverse(head)  # 遍历链表