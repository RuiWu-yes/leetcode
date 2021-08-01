# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 实现堆
# @Content : 实现堆数据结构


class Heap:
    def __init__(self, length):
        self.heap = [0] * (length + 1)  # 用数组来实现堆
        self.size = 0  # 堆中元素的个数

    def push(self, val):
        if self.size == len(self.heap) - 1:  # 堆中元素已经填满
            return False
        self.size += 1
        self.heap[self.size] = val
        self.shift_up(self.size)
        return True

    def pop(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.shift_down(1)
        return val

    def peek(self):
        return self.heap[1]

    def shift_up(self, i):
        val = self.heap[i]
        while i >> 1 > 0:  # i >> 1 相当于 i 除 2
            parent = i >> 1
            if val < self.heap[parent]:  # 比父节点值小
                self.heap[i] = self.heap[parent]
                i = parent
            else:
                break
        self.heap[i] = val

    def shift_down(self, i):
        val = self.heap[i]
        while i << 1 <= self.size:  # i << 1 相当于 i 乘 2
            child = i << 1
            if child != self.size and self.heap[child+1] < self.heap[child]:
                child += 1
            if val > self.heap[child]:
                self.heap[i] = self.heap[child]
                i = child
            else:
                break
        self.heap[i] = val