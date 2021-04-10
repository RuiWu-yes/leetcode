# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现计数排序 O(n+k)
# 介绍：计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
#      作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
# 描述：1) 找出待排序的数组中最大和最小的元素；
#      2) 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
#      3) 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
#      4) 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。


class Sort:
    def countsort(self, nums):
        pass


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.countsort(nums)
    print('排序后:', nums)