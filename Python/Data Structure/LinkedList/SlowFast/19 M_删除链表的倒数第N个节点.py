# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 19 删除链表的倒数第N个节点
# @Content : 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# @Explain : 给定的 n 保证是有效的。
#      进阶： 你能尝试使用一趟扫描实现吗？ O(N)时间复杂度


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 我们的思路还是使用快慢指针，让快指针先走 n 步，然后快慢指针开始同速前进。
        # 这样当快指针走到链表末尾 None 时，慢指针所在的位置就是倒数第 n 个链表节点（n 不会超过链表长度）。
        # 1->2->3->4, n = 2
        # s     f
        #    s     f
        slow = fast = head
        # 快指针先前进 n 步
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            # 如果此时快指针走到头了，
            # 说明倒数第 n 个节点就是第一个节点
            return head.next
        # 让慢指针和快指针同步向前
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # slow.next 就是倒数第 n 个节点，删除它
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    from libs import linked_list as ll

    # 给定一个链表: 1->2->3->4->5, 和 n = 2.
    # 当删除了倒数第二个节点后，链表变为 1->2->3->5.
    head = ListNode(1)
    sll = ll.SingleLinkedList(head)
    for x in [2, 3, 4, 5]: sll.append(x)
    n = 2

    sol = Solution()
    res = ll.SingleLinkedList(sol.removeNthFromEnd(head, n)).traverse()
    print(res)