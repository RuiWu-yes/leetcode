# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现插入排序 O(N^2)
# 介绍：插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。
#      它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 描述：一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
#          1) 从第一个元素开始，该元素可以认为已经被排序；
#          2) 取出下一个元素，在已经排序的元素序列中从后向前扫描；
#          3) 如果该元素（已排序）大于新元素，将该元素移到下一位置；
#          4) 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
#          5) 将新元素插入到该位置后；
#          6) 重复步骤2~5。

class Sort:
    def insertionsort(self, nums):
        for j in range(1, len(nums)):
            i = j
            while i > 0:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                    i -= 1
                else:
                    break


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.insertionsort(nums)
    print('排序后:', nums)