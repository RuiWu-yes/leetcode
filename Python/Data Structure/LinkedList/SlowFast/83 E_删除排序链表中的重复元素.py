# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 83 删除排序链表中的重复元素
# @Content : 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head: return
        slow = fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next  # 此时，slow == fast
            fast = fast.next
        slow.next = None  # 断开与后面重复元素的连接
        return head


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  输出: 1->2
    # 输入: 1->1->2
    head1 = ListNode(1)
    sll1 = ll.SingleLinkedList(head1)
    for x in [1, 2]: sll1.append(x)

    # case2  输出: 1->2->3
    # 输入: 1->1->2->3->3
    head2 = ListNode(1)
    sll2 = ll.SingleLinkedList(head2)
    for x in [1, 2, 3, 3]: sll2.append(x)

    sol = Solution()
    res1 = ll.SingleLinkedList(sol.deleteDuplicates(head1)).traverse()
    res2 = ll.SingleLinkedList(sol.deleteDuplicates(head2)).traverse()
    print('case1:', res1)
    print('case2:', res2)