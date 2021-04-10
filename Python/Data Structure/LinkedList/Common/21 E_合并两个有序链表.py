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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode or None:
        # 递归法
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1  # 由于是l1接到l2最左边，显然此时l1节点为头节点
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2  # 由于是l2接到l1最左边，显然此时l2节点为头节点

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode or None:
        # 迭代法
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 else l2
        return prehead.next


if __name__ == '__main__':
    from libs import linked_list as ll

    def traverse(root):
        res = []
        while root:
            res.append(root.val)
            root = root.next
        return res

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
    l1_2 = None
    l2_2 = None

    # case3  res = [0]
    # l1_3 = [], l2_3 = [0]
    l1_3 = None
    l2_3 = ListNode(0)

    sol = Solution()
    res1 = sol.mergeTwoLists(l1_1, l2_1)
    res2 = sol.mergeTwoLists(l1_2, l2_2)
    res3 = sol.mergeTwoLists(l1_3, l2_3)

    # res1 = sol.mergeTwoLists2(l1_1, l2_1)
    # res2 = sol.mergeTwoLists2(l1_2, l2_2)
    # res3 = sol.mergeTwoLists2(l1_3, l2_3)

    print('case1:', traverse(res1))
    print('case2:', traverse(res2))
    print('case3:', traverse(res3))