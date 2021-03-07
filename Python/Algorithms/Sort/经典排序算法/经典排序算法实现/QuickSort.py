# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现快速排序 O(NlogN)
# 介绍：快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，
#      则可分别对这两部分记录继续进行排序，以达到整个序列有序。
# 描述：快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
#         1) 从数列中挑出一个元素，称为 “基准”（pivot）；
#         2) 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
#            在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
#         3) 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。


class Sort:
    def quicksort(self, begin, end, nums):
        if begin >= end:
            return
        pivot_index = self.partition(begin, end, nums)
        self.quicksort(begin, pivot_index - 1, nums)
        self.quicksort(pivot_index + 1, end, nums)

    def partition(self, begin, end, nums):
        pivot = nums[begin]
        mark = begin
        for i in range(begin + 1, end + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[begin], nums[mark] = nums[mark], nums[begin]
        return mark


if __name__ == '__main__':
    begin = 0
    end = 6
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.quicksort(begin, end, nums)
    print('排序后:', nums)