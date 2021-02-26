# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 92 反转链表 II
# @Content : 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#            1 ≤ m ≤ n ≤ 链表长度。


# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        :param head:
        :param m:
        :param n:
        :return: 从head头节点开始遍历
                 1) 当遍历的节点没有到达m位置，此时返回self.reverseBetween(head.next, m-1, n-1)的结果
                 2) 当遍历的节点到达m位置，此时返回self.reverseN(head, n)的结果
        '''
        # base case
        if m == 1: return self.reverseN(head, n)
        # 前进到反转的起点触发 base case
        # head.next是相对于本层reverseBetween传递的head节点，会接收下一层的self.reverseN(head, n)的last节点 或者 下一层的head
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    def reverseN(self, head, n):
        '''
        :param head:
        :param n:
        :return: 从head节点开始遍历
                 1) 当遍历的节点没有到达n位置，此时只是做链表翻转操作
                 2) 当遍历的节点到达n位置，即找到了需要最终返回的节点，return head最终会传递给last参数
        '''
        # 反转链表前 N 个节点， m = 1
        # 当n = 1时，表示已经到了指定索引区间[m, n]的末端了，返回head本身，最终会传递给last参数
        if n == 1: return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        successor = head.next.next
        # 以head.next为开头的链表已经完成翻转，那么head.next.next正确指向后继节点
        head.next.next = head
        head.next = successor
        return last


if __name__ == '__main__':
    from libs import linked_list as ll

    # case1
    # 输入: 1->2->3->4->5->NULL, m = 2, n = 4
    head = ListNode(1)
    sll = ll.SingleLinkedList(head)
    for x in [2, 3, 4, 5]: sll.append(x)
    m = 2
    n = 4
    # 输出: 1->4->3->2->5->NULL

    sol = Solution()
    head1 = sol.reverseBetween(head, m, n)
    res1 = ll.SingleLinkedList(head1)
    print('case1:', end=' ')
    res1.traverse()