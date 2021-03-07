# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现选择排序 O(N^2)
# 介绍：选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，
#      存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以
#      此类推，直到所有元素均排序完毕。
# 描述：n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：
#         1) 初始状态：无序区为R[1..n]，有序区为空；
#         2) 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无
#            序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为
#            记录个数增加1个的新有序区和记录个数减少1个的新无序区；
#         3) n-1趟结束，数组有序化了。


class Sort:
    def selectionsort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.selectionsort(nums)
    print('排序后:', nums)