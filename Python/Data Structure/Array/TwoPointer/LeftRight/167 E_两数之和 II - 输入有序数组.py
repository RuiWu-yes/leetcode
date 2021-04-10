# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 167 两数之和 II - 输入有序数组
# @Content : 给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
#            函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# @Explain : 1) 返回的下标值（index1 和 index2）不是从零开始的。
#            2) 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。


class Solution:
    def twoSum(self, numbers, target: int):
        # 左右双指针
        left, right = 0, len(numbers) - 1
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left+1, right+1]
            elif sums < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    # case1  res = [1, 2]
    # 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    numbers = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    res = sol.twoSum(numbers, target)
    print(res)