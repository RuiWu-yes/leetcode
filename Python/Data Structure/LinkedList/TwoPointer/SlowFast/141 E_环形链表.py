# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 141 环形链表
# @Content : 给定一个链表，判断链表中是否有环。
#            如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
#            为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
#            如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#            如果链表中存在环，则返回 true 。 否则，返回 false 。
#      进阶 : 你能用 O(1)（即，常量）内存解决此问题吗？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle1(self, head: ListNode) -> bool:
        # 快慢指针
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False
        while head.next and head.val != None:
            head.val = None  # 遍历的过程中将值置空
            head = head.next
        if not head.next:  # 如果碰到空发现已经结束，则无环
            return False
        return True  # 否则有环


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
    res1_1 = sol.hasCycle1(head1)
    res1_2 = sol.hasCycle2(head1)
    res2_1 = sol.hasCycle1(head2)
    res2_2 = sol.hasCycle2(head2)
    res3_1 = sol.hasCycle1(head3)
    res3_2 = sol.hasCycle2(head3)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)
    print('case3:', res3_1, res3_2)