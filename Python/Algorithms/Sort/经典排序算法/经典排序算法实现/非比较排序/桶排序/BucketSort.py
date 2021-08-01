# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现桶排序 O(N+k)
# 介绍：桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
#      桶排序的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
# 描述：1) 设置一个定量的数组当作空桶；
#      2) 遍历输入数据，并且把数据一个一个放到对应的桶里去；
#      3) 对每个不是空的桶进行排序；
#      4) 从不是空的桶里把排好序的数据拼接起来。

# 计数排序与桶排序都是以牺牲空间换时间，虽然很快，但由于可能产生大量的空位置导致内存增大，尤其是计数排序。
# 桶排序中尽量使每个桶中的元素个数均匀分布最好


class Sort:
    def bucketsort(self, nums):
        # 找到最大最小值
        min_num = min(nums)
        max_num = max(nums)
        # 桶的大小
        bucket_range = (max_num - min_num) / len(nums)
        # 桶数组
        count_list = [[] for _ in range(len(nums) + 1)]
        # 向桶数组填数
        for i in nums:
            count_list[int((i - min_num) // bucket_range)].append(i)
        nums.clear()
        # 回填，这里桶内部排序直接调用了sorted
        for i in count_list:
            for j in sorted(i):
                nums.append(j)


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.bucketsort(nums)
    print('排序后:', nums)