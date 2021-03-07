# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 21 合并两个有序链表
# @Content : 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  res = [1, 1, 2, 3, 4, 4]
    # l1_1 = [1, 2, 4], l2_1 = [1, 3, 4]
    l1_1 = ListNode(1)
    sll = ll.SingleLinkedList(l1_1)
    for x in [2, 4]: sll.append(x)
    l2_1 = ListNode(1)
    sll = ll.SingleLinkedList(l2_1)
    for x in [3, 4]: sll.append(x)

    # case2  res = []
    # l1_2 = [], l2_2 = []
    l1_2 = ListNode()
    l2_2 = ListNode()

    # case3  res = [0]
    # l1_3 = [], l2_3 = [0]
    l1_3 = ListNode()
    l2_3 = ListNode(0)

    sol = Solution()
    res1 = sol.mergeTwoLists(l1_1, l2_1)
    res2 = sol.mergeTwoLists(l1_2, l2_2)
    res3 = sol.mergeTwoLists(l1_3, l2_3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)