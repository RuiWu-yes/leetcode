# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现堆排序 O(NlogN)
# 介绍：堆排序是指利用堆这种数据结构所设计的一种排序算法。
#      堆通常是一个可以被看做一棵树的数组对象。
#      堆总是满足下列性质：
#         1) 堆中某个结点的值总是不大于或不小于其父结点的值；
#         2) 堆总是一棵完全二叉树。
#      将根结点最大的堆叫做最大堆或大根堆，根结点最小的堆叫做最小堆或小根堆
# 描述：1) 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
#      2) 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
#      3) 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，
#         得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
length = 0


class Sort:
    def buildMaxHeap(self, nums):
        # 建立最大堆
        global length
        length = len(nums)

        for i in range(length // 2, -1, -1):  # i：可认为是根节点
            self.heapify(nums, i)

    def heapify(self, nums, i):
        # 堆调整
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i  # 根(默认是最大)

        if left < length and nums[left] > nums[largest]:  # 左
            # 如果左节点存在
            # 将左节点的值与根节点的值去比较:
            #    如果largest(此时是根节点)值小于左节点的值，不满足最大堆，将左节点标记为最大值节点
            #    否则不做任何处理
            largest = left
        if right < length and nums[right] > nums[largest]:  # 右
            # 如果右节点存在
            # 将右节点的值与根节点的值去比较:
            #    如果largest(此时是根节点或者是左节点)值小于右节点的值，不满足最大堆，将右节点标记为最大值节点
            #    否则不做任何处理
            largest = right
        if largest != i:
            # 如果记录最大节点的largest不等于根节点，说明发现不满足最大堆的节点，将原来根节点nums[i]与nums[largest]进行交换
            nums[i], nums[largest] = nums[largest], nums[i]
            # 递归到largest(此时是交换后的“根”节点)节点，再进行堆调整
            self.heapify(nums, largest)

    def heapsort(self, nums):
        self.buildMaxHeap(nums)  # 将nums构建成最大堆，此堆为初始的无序区
        for i in range(len(nums)-1, 0, -1):
            # 将堆顶元素R1与最后一个元素Rn交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn), 且满足 R[1,2…n-1] <= R[n]
            nums[0], nums[i] = nums[i], nums[0]
            # 新的无序区(R1,R2,……Rn-1)的长度 - 1
            global length
            length -= 1
            # 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆
            self.heapify(nums, 0)
        return nums


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.heapsort(nums)
    print('排序后:', nums)