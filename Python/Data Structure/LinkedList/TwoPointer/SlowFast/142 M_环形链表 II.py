# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 142 环形链表 II
# @Content : 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#            为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
#            如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
# @Explain : 不允许修改给定的链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        if not fast or not fast.next:
            return
        # 快慢指针相遇的节点 与 head节点 离环交点(junction)的距离一样
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow

if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  res = true
    head1 = ListNode(3)
    sll1 = ll.SingleLinkedList(head1)
    for x in [2, 0, -4]: sll1.append(x)
    head1 = sll1.addcycle(head1, 1, 3)

    # case2  res = true
    head2 = ListNode(1)
    sll2 = ll.SingleLinkedList(head2)
    for x in [2]: sll2.append(x)
    head2 = sll2.addcycle(head2, 0, 1)

    # case3  res = false
    head3 = ListNode(1)

    sol = Solution()
    res1 = sol.detectCycle(head1)
    res2 = sol.detectCycle(head2)
    res3 = sol.detectCycle(head3)
    print('case1:', res1.val if res1 else None)
    print('case2:', res2.val if res2 else None)
    print('case3:', res3.val if res3 else None)