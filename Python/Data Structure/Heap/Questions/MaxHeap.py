# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 实现最大堆
# @Content : 实现最大堆数据结构


class MaxHeap:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [0] * maxsize  # 初始化一个数组去实现堆
        self._count = 0  # 对节点个数进行计数

    def __len__(self):
        return self._count

    def push(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value  # count为节点数个数，如果用count值作为索引的话，刚好相当于在最后一个节点后添加一个节点
        self._siftup(self._count)  # 维持堆的特性
        self._count += 1

    def pop(self):
        # 注意: pop方法会返回被删除的值
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]  # 记录即将删除的根节点的值
        self._count -= 1  # 计数先减1的好处：(1)本身就要删除根节点，所以节点数减1 (2)删除根节点操作前减1的值相当于最后一个节点在数组的索引
        self._elements[0] = self._elements[self._count]  # 用堆中最后一个节点替换要删除的根节点
        self._siftdown(0)  # 维持堆特性
        return value

    def peek(self):
        return self._elements[0]

    def _siftup(self, idx):
        if idx > 0:  # 等于0没有父节点
            parent = (idx - 1) // 2
            if self._elements[idx] > self._elements[parent]:  # 如果插入的值大于 parent，一直交换
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._siftup(parent)  # 递归

    def _siftdown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        if left < self._count and \
           self._elements[left] >= self._elements[largest] and \
           self._elements[left] >= self._elements[right]:  # 左子节点比右子节点和父节点都大
            largest = left
        elif right < self._count and \
            self._elements[right] >= self._elements[largest]:  # 右子节点比父节点大
            largest = right
        if largest != idx:  # 不等于说明上面的if触发了
            self._elements[idx], self._elements[largest] = self._elements[largest], self._elements[idx]
            self._siftdown(largest)


if __name__ == '__main__':
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.push(i)
    print(h.__len__())
    for i in range(n):
        h.pop()
    print(h.__len__())
