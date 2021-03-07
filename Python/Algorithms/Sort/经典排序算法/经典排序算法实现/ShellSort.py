# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现希尔排序 O(N^2)
# 介绍：1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，
#      它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
# 描述：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
#         1) 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
#         2) 按增量序列个数k，对序列进行k 趟排序；
#         3) 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。
#            仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


class Sort:
    def shellsort(self, nums):
        n = len(nums)
        gap = int(n / 2)
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = int(gap / 2)


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.shellsort(nums)
    print('排序后:', nums)