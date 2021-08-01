# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 146 LRU 缓存机制
# @Content : 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
#            实现 LRUCache 类：
#                1) LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
#                2) int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#                3) void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
#                   当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#      进阶 : 你是否可以在 O(1) 时间复杂度内完成这两种操作？


# ----------------------------------------------------------------------------------------------------------------
# 在 Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict，只需要短短的几行代码就可以完成本题
from collections import OrderedDict


class LRUCache1(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# ----------------------------------------------------------------------------------------------------------------
# 哈希表 + 双向链表
# LRU 缓存机制可以通过哈希表辅以双向链表实现，我们用一个哈希表和一个双向链表维护所有在缓存中的键值对。
#   * 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
#   * 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
# 这样以来，我们首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，即可在O(1) 的时间内完成 get 或者 put 操作。
# 具体的方法如下：
# 1) 对于 get 操作，首先判断 key 是否存在：
#   * 如果 key 不存在，则返回−1；
#   * 如果 key 存在，则 key 对应的节点是最近被使用的节点。通过哈希表定位到该节点在双向链表中的位置，
#     并将其移动到双向链表的头部，最后返回该节点的值。
# 2) 对于 put 操作，首先判断 key 是否存在：
#   * 如果 key 不存在，使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，并将 key
#     和该节点添加进哈希表中。然后判断双向链表的节点数是否超出容量，如果超出容量，则删除双向链表的尾
#     部节点，并删除哈希表中对应的项；
#   * 如果 key 存在，则与 get 操作类似，先通过哈希表定位，再将对应的节点的值更新为 value，并将该
#     节点移到双向链表的头部。
# 上述各项操作中，访问哈希表的时间复杂度为O(1)，在双向链表的头部添加节点、在双向链表的尾部删除节点的复杂度也为O(1)。
# 而将一个节点移到双向链表的头部，可以分成「删除该节点」和「在双向链表的头部添加节点」两步操作，都可以在O(1) 时间内完成。
#
# 小贴士
# 在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限，这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在。
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None  # 前驱指针
        self.next = None  # 后继指针

class LRUCache2:
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点标记界限，这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity  # 缓存的容量大小
        self.size = 0  # 缓存的元素个数

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                # 缓存的元素个数减1
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value  # 修改值 #
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    lRUCache = LRUCache2(2)
    lRUCache.put(1, 1)         # 缓存是 {1=1}
    lRUCache.put(2, 2)         # 缓存是 {1=1, 2=2}
    res1 = lRUCache.get(1)     # 返回 1
    lRUCache.put(3, 3)         # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    res2 = lRUCache.get(2)     # 返回 -1 (未找到)
    lRUCache.put(4, 4)         # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    res3 = lRUCache.get(1)     # 返回 -1 (未找到)
    res4 = lRUCache.get(3)     # 返回 3
    res5 = lRUCache.get(4)     # 返回 4

    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)