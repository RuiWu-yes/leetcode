# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 752 打开转盘锁
# @Content : 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
#            每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#            锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#            列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#            字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
import collections


class Solution:
    def openLock1(self, deadends, target):
        # 单向BFS
        deadends = set(deadends)
        if target in deadends: return -1
        cout = 0
        deque = collections.deque(['0000'])
        visited = {'0000'}
        while deque:
            for _ in range(len(deque)):
                cur = deque.popleft()
                if cur in deadends: continue
                if cur == target: return cout
                for i in range(4):
                    new_plus = self.plusOne(cur, i)
                    if new_plus not in visited:
                        deque.append(new_plus)
                        visited.add(new_plus)
                    new_minus = self.minusOne(cur, i)
                    if new_minus not in visited:
                        deque.append(new_minus)
                        visited.add(new_minus)
            cout += 1
        return -1

    def openLock2(self, deadends, target):
        # 双向BFS
        deadends = set(deadends)
        fore, back, visited = {'0000'}, {target}, set()  # 创建空集合一定要用set()而不是{}，因为后者用来创建空字典
        cout = 0
        while fore and back:
            temp = set()  # 由于元素添加到集合是乱序的，因此需要临时temp存下一层节点
            if len(fore) > len(back):  # 如果前方向和后方向长度不同，取短的那个方向进行BFS，可以遍历更少节点，更快的两方向相遇返回结果
                fore, back = back, fore
            for cur in fore:
                if cur in deadends: continue
                if cur in back: return cout  # 表示双向BFS相遇了，返回最终结果
                visited.add(cur)  # 不是用队列去添加下一层，然后直接遍历队列；而是直接遍历集合，所以遍历一个元素添加一个元素到查重集
                for i in range(4):
                    new_plus = self.plusOne(cur, i)
                    if new_plus not in visited:
                        temp.add(new_plus)
                    new_minus = self.minusOne(cur, i)
                    if new_minus not in visited:
                        temp.add(new_minus)
            cout += 1
            # fore = back  # 交换方向进行BFS
            # back = temp
            fore, back = back, temp

        return -1

    def plusOne(self, s, idx):
        ls = list(s)
        if ls[idx] == '9':
            ls[idx] = '0'
        else:
            ls[idx] = str(int(ls[idx]) + 1)
        return ''.join(ls)

    def minusOne(self, s, idx):
        ls = list(s)
        if ls[idx] == '0':
            ls[idx] = '9'
        else:
            ls[idx] = str(int(ls[idx]) - 1)
        return ''.join(ls)


if __name__ == '__main__':
    # case1  res = 6
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

    # # case2  res = 1
    # deadends = ["8888"]
    # target = "0009"

    # # case3  res = -1
    # deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    # target = "8888"

    s = Solution()
    res1 = s.openLock1(deadends, target)
    res2 = s.openLock2(deadends, target)
    print('单向BFS：', res1)
    print('双向BFS：', res2)