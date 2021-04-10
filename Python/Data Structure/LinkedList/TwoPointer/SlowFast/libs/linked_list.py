class ListNode():
    def __init__(self, x):
        # 元素域
        self.val = x
        # 链接域
        self.next = None


class SingleLinkedList():
    def __init__(self, node=None):
        self.__head = node

    def __len__(self):
        # 游标，用来遍历链表
        cur = self.__head
        # 记录遍历次数
        count = 0
        # 当前节点为None则说明已经遍历完毕
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        # 头节点不为None则不为空
        return self.__head == None

    def prepend(self, val):
        """
        头插法
        先让新节点的next指向头节点
        再将头节点替换为新节点
        顺序不可错，要先保证原链表的链不断，否则头节点后面的链会丢失
        """
        node = ListNode(val)
        node.next = self.__head
        self.__head = node

    def append(self, val):
        """尾插法"""
        node = ListNode(val)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, val):
        # 应对特殊情况
        if pos <= 0:
            self.prepend(val)
        elif pos > len(self) - 1:
            self.append(val)
        else:
            node = ListNode(val)
            prior = self.__head
            count = 0
            # 在插入位置的前一个节点停下
            while count < (pos - 1):
                prior = prior.next
                count += 1
            # 先将插入节点与节点后的节点连接，防止链表断掉，先链接后面的，再链接前面的
            node.next = prior.next
            prior.next = node

    def addcycle(self, head, pos1, pos2):
        '''
           head: 头节点
           pos1: 成环节点位置1
           pos2：成环节点位置2
        '''
        junction = None
        count = 0
        node = head
        while node:
            if count == pos1:
                junction = node
            if count == pos2:
                node.next = junction
                break
            count += 1
            node = node.next
        return head

    def remove(self, val):
        cur = self.__head
        prior = None
        while cur:
            if val == cur.val:
                # 判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                break
            # 还没找到节点，有继续遍历
            else:
                prior = cur
                cur = cur.next

    def search(self, val):
        cur = self.__head
        while cur:
            if val == cur.val:
                return True
            cur = cur.next
        return False

    def traverse(self):
        cur = self.__head
        list = []
        while cur:
            list.append(cur.val)
            cur = cur.next
        return list