# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 合并k个有序数组
# @Content : 有k个长度可能不同的有序数组，将其合并成一个有序数组
# 三种思路：1) 申请一个数组，将所有的元素添加到该数组中，使用sort()函数，直接进行排序
#         2) 归并排序: 两两归并
#         3) 构造小根堆
from typing import List
import heapq


class Solution2:
    # 思路二：归并排序
    def sortNArray(self, nums):
        # 递归结束条件
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2  # 取中间位置
        left = self.sortNArray(nums[:mid])
        right = self.sortNArray(nums[mid:])

        return self.sort_list(left[0], right[0])  # 要传入的参数是数组中第一个索引处的值

    def sort_list(self, left, right):
        res = []
        a, b = 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                res.append(left[a])
                a += 1
            else:
                res.append(right[b])
                b += 1
        # 因为存在一个到终点后，另一个还没到终点，这时就需要将没到终点的剩下的值添加到数组中
        while a < len(left):
            res.append(left[a])
            a += 1
        while b < len(right):
            res.append(right[b])
            b += 1
        return [res]  # 将一维数组二维化


class Solution3:
    # 思路三：构造小根堆
    # 首先遍历所有的数组，确定最终所有元素的个数(count)；
    # 创建一个大小为count的数组用来保存最终结果，再创建一个大小为K的小根堆；（小根堆保存的元素类型，是结构体）
    # 先将每个数组的第一个元素插入到小根堆中，进行一次堆排序；
    # 重复下面的操作，直至元素全部插入结果集中：
    #   a. 取出堆顶元素(堆中最小元素),保存到结果中；
    #   b. 将堆顶元素所在数组的下一个元素替换到堆顶，如果堆顶元素是其所在数组的最后一个,将堆顶元素替换成INT_MAX;
    #   c. 进行一次堆排序；
    def sortNArray1(self, nums: List[List[int]]) -> List:
        # 库函数调用
        # heapq.merge() 需要所有输入序列必须是排过序的。 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。
        # 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。
        sorted_list = [i for i in heapq.merge(*nums)]
        return sorted_list

    def sortNArray2(self, nums: List[List[int]]) -> List:
        heap = []
        for i, arr in enumerate(nums):
            heap.append((arr.pop(0), i))
        heapq.heapify(heap)  # 将heap转换成最小堆

        result = []
        while heap:
            value, index = heapq.heappop(heap)  # 将堆顶层元素出堆
            result.append(value)  # 将顶层元素追加
            # 根据索引获取对应array的剩余元素
            if nums[index]:
                # 如果存在下一个元素,则将该元素及索引入堆
                heapq.heappush(heap, (nums[index].pop(0), index))
        return result


if __name__ == '__main__':
    # case1  res = [2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 17, 20, 25, 30]
    nums1 = [[5, 10, 13, 17], [2, 4, 7, 8, 25], [3, 6, 11, 15, 20, 30]]

    sol2, sol3 = Solution2(), Solution3()
    res1 = sol2.sortNArray(nums1), sol3.sortNArray1(nums1), sol3.sortNArray2(nums1)
    print(res1)