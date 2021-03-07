# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现归并排序 O(NlogN)
# 介绍：归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
#      将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，
#      称为2-路归并。
# 描述：1) 把长度为n的输入序列分成两个长度为n/2的子序列；
#      2) 对这两个子序列分别采用归并排序；
#      3) 将两个排序好的子序列合并成一个最终的排序序列。


class Sort:
    # 将数组分开
    def mergesort(self, nums):
        mid = len(nums) // 2
        # 如果列表已经是最小单元，返回这个列表
        if mid <= 1:
            return nums
        # 对nums进行“分”的处理
        return self.merge(self.mergesort(nums[0:mid]), self.mergesort(nums[mid:]))

    # 合并两个数据，产生一个已经排序好的新的数组
    def merge(self, left, right):
        # 设定临时数组
        result = []
        # 设定指向两个数组的指针，起始为0
        i = j = 0
        while i < len(left) and j < len(right):
            # 如果left的下标i > right的下标j
            if left[i] >= right[j]:
                # 将right中的第j个元素放到result中
                result.append(right[j])
                # j的下标右移一位
                j += 1
            else:
                result.append(left[i])
                i += 1

        result += left[i:]
        result += right[j:]
        return result


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.mergesort(nums)
    print('排序后:', nums)