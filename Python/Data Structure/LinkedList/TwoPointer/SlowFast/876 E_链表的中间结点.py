# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 876 链表的中间结点
# @Content : 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#            如果有两个中间结点，则返回第二个中间结点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  res = [3, 4, 5]
    # 输入：1->2->3->4->5->NULL
    # 输出：此列表中的结点 3 (序列化形式：[3, 4, 5])
    #      返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3, 4, 5])。
    head1 = ListNode(1)
    sll1 = ll.SingleLinkedList(head1)
    for x in [2, 3, 4, 5]: sll1.append(x)

    # case2  res = [4, 5, 6]
    # 输入：1->2->3->4->5->6->NULL
    # 输出：此列表中的结点 4 (序列化形式：[4, 5, 6])
    head2 = ListNode(1)
    sll2 = ll.SingleLinkedList(head2)
    for x in [2, 3, 4, 5, 6]: sll2.append(x)

    sol = Solution()
    res1 = ll.SingleLinkedList(sol.middleNode(head1)).traverse()
    res2 = ll.SingleLinkedList(sol.middleNode(head2)).traverse()
    print('case1:', res1)
    print('case2:', res2)