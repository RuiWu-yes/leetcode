# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 234 回文链表
# @Content : 请判断一个链表是否为回文链表。
#      进阶 : 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
        # 方法一：借助二叉树后序遍历的思路，不需要显式反转原始链表也可以倒序遍历链表
        left = head
        def traverse(right):
            nonlocal left
            if not right: return True
            res = traverse(right.next)
            # 后序遍历代码
            res = res and right.val == left.val
            left = left.next
            return res
        return traverse(head)

    def isPalindrome2(self, head: ListNode) -> bool:
        # 方法二: (最优方法)时间复杂度 O(N)，空间复杂度 O(1)
        # 0) 定义反转链表函数
        def reverse(head):
            pre, cur = None, head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        # 1) 先通过「双指针技巧」中的快慢指针来找到链表的中点：
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2) 如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步
        if fast: slow = slow.next
        # 3) 从slow开始反转后面的链表，现在就可以开始比较回文串了
        left = head
        right = reverse(slow)
        # 4) 判断left，right是否相同。相同则为回文链表，否则不为回文链表
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1  输入：1->2->None  输出：False
    head1 = ListNode(1)
    sll = ll.SingleLinkedList(head1)
    for x in [2]: sll.append(x)
    # case2  输入：1->2->2->1->None  输出：True
    head2 = ListNode(1)
    sll = ll.SingleLinkedList(head2)
    for x in [2, 2, 1]: sll.append(x)

    sol = Solution()
    res1_1 = sol.isPalindrome1(head1)
    res1_2 = sol.isPalindrome2(head1)
    print('case1：', res1_1, res1_2)

    res2_1 = sol.isPalindrome1(head2)
    res2_2 = sol.isPalindrome2(head2)
    print('case2：', res2_1, res2_2)