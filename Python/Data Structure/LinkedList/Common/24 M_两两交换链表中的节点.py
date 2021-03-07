# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 24 两两交换链表中的节点
# @Content : 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#            你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归法
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  res = [2, 1, 4, 3]
    head1 = ListNode(1)
    sll = ll.SingleLinkedList(head1)
    for x in [2, 3, 4]: sll.append(x)

    # case2  res = []
    head2 = []

    # case3  res = [1]
    head3 = ListNode(1)

    sol = Solution()
    res1 = sol.swapPairs(head1)
    res2 = sol.swapPairs(head2)
    res3 = sol.swapPairs(head3)

    res1 = ll.SingleLinkedList(res1)
    print('case1:', end=" ")
    res1.traverse()

    # res2 = ll.SingleLinkedList(res2)
    # print('case2:', end=" ")
    # res2.traverse()

    # res3 = ll.SingleLinkedList(res3)
    # print('case3:', end=" ")
    # res3.traverse()