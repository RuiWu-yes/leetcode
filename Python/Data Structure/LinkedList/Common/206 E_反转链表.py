# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 206 反转链表
# @Content : 反转一个单链表。
#      进阶 : 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        # 递归
        if not head.next: return head
        last = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseList2(self, head: ListNode) -> ListNode:
        # 迭代
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1
    # 输入：1->2->3->4->5->NULL
    head = ListNode(1)
    sll = ll.SingleLinkedList(head)
    for x in [2, 3, 4, 5]: sll.append(x)
    # 输出：5->4->3->2->1->NULL

    sol = Solution()
    # # 递归法
    # head1 = sol.reverseList1(head)
    # for i in range(5):
    #     print('递归法：', head1.val, end=' ') if i == 0 else print(head1.val, end=' ')
    #     head1 = head1.next

    # 迭代法
    head2 = sol.reverseList2(head)
    for i in range(5):
        print('迭代法：', head2.val, end=' ') if i == 0 else print(head2.val, end=' ')
        head2 = head2.next