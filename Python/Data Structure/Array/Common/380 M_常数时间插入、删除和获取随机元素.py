# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 380 常数时间插入、删除和获取随机元素
# @Content : 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#            1) insert(val)：当元素 val 不存在时，向集合中插入该项。
#            2) remove(val)：元素 val 存在时，从集合中移除该项。
#            3) getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
import random
from collections import defaultdict


class RandomizedSet:
    # 对于 getRandom 方法，如果想「等概率」且「在 O(1) 的时间」取出元素，一定要满足：底层用数组实现，且数组必须是紧凑的。
    # 这样我们就可以直接生成随机数作为索引，从数组中取出该随机索引对应的元素，作为随机元素。
    # 但如果用数组存储元素的话，插入，删除的时间复杂度怎么可能是 O(1) 呢？
    #    可以做到！对数组尾部进行插入和删除操作不会涉及数据搬移，时间复杂度是 O(1)。
    # 所以，如果我们想在 O(1) 的时间删除数组中的某一个元素 val，可以先把这个元素交换到数组的尾部，然后再 pop 掉。
    # 交换两个元素必须通过索引进行交换对吧，那么我们需要一个哈希表 valToIndex 来记录每个元素值对应的索引。
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []        # 存储元素的值
        self.valToIndex = defaultdict(lambda: -1)  # 记录每个元素对应在 nums 中的索引

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # 若 val 已存在，不用再插入
        if self.valToIndex[val] != -1:
            return False
        # 若 val 不存在，插入到 nums 尾部，
        # 并记录 val 对应的索引值
        self.valToIndex[val] = len(self.nums)  # 索引没有数组长度-1，是因为此时还没有尾插入元素，此时数组长度就等于添加val元素的索引
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 若 val 不存在，不用再删除
        if self.valToIndex[val] == -1:
            return False
        # 先拿到 val 的索引
        index = self.valToIndex[val]
        # 将最后一个元素对应的索引修改为 index
        self.valToIndex[self.nums[-1]] = index
        # 交换 val 和最后一个元素
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 在数组中删除元素 val
        self.nums.pop()
        # 删除元素 val 对应的索引
        del self.valToIndex[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # 随机获取 nums 中的一个元素
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    # 示例 :
    # 初始化一个空的集合。
    randomSet = RandomizedSet()

    # 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    res1 = randomSet.insert(1)

    # 返回 false ，表示集合中不存在 2 。
    res2 = randomSet.remove(2)

    # 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    res3 = randomSet.insert(2)

    # getRandom 应随机返回 1 或 2 。
    res4 = randomSet.getRandom()

    # 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    res5 = randomSet.remove(1)

    # 2 已在集合中，所以返回 false 。
    res6 = randomSet.insert(2)

    # 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
    res7 = randomSet.getRandom()

    print(res1, res2, res3, res4, res5, res6, res7)