# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Content : 实现基数排序 O(n+k)
# 介绍：基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
#      有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
# 描述：1) 取得数组中的最大数，并取得位数
#      2) arr为原始数组，从最低位开始取每个位组成radix数组
#      3) 对radix进行计数排序（利用计数排序适用于小范围数的特点）


class Sort:
    def radixsort(self, nums, maxDigit):
        pass


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1, 0]
    print('排序前:', nums)

    sort = Sort()
    sort.radixsort(nums)
    print('排序后:', nums)