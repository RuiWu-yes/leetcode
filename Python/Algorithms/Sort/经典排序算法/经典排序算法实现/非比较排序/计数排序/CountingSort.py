# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现计数排序 O(n+k)
# 介绍：计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
#      作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
# 思想：对每一个输入的元素a[i]，确定小于 a[i] 的元素个数。所以可以直接把 a[i] 放到它输出数组中的位置上。
#      假设有5个数小于 a[i]，所以 a[i] 应该放在数组的第6个位置上。
# 描述：1) 找出待排序的数组中最大和最小的元素；
#      2) 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
#      3) 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
#      4) 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
# 计数排序是桶排序的一种特殊情况，可以把计数排序当成每个桶里只有一个元素的情况。

# 计数排序与桶排序都是以牺牲空间换时间，虽然很快，但由于可能产生大量的空位置导致内存增大，尤其是计数排序。
# 桶排序中尽量使每个桶中的元素个数均匀分布最好


class Sort:
    def countsort(self, nums):
        # 找到最大最小值
        min_num = min(nums)
        max_num = max(nums)
        # 计数列表
        count_list = [0] * (max_num - min_num + 1)
        # 计数
        for i in nums:
            count_list[i - min_num] += 1
        nums.clear()
        # 填回
        for i, v in enumerate(count_list):
            while v != 0:
                nums.append(i + min_num)
                v -= 1


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.countsort(nums)
    print('排序后:', nums)