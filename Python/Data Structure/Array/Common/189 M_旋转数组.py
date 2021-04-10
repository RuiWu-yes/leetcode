# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 189 旋转数组
# @Content : 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#      进阶 ：1) 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#            2) 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路一
        # 循环替代，第一个替代下一个，依次循环。计算循环遍历的个数，循环所有位置。
        k = k % len(nums)
        cnt = 0
        start = 0
        while cnt < len(nums):
            current = start
            pre = nums[start]
            while True:
                nxt = (current + k) % len(nums)
                nums[nxt], pre = pre, nums[nxt]
                current = nxt
                cnt += 1
                if start == current:
                    break
            start += 1

    def rotate2(self, nums: List[int], k: int) -> None:
        # 思路二
        # 三次翻转，先整体翻转，然后根据K的位置前后局部翻转。
        n = len(nums)
        k %= n
        # [:]和copy.copy()都属于“浅拷贝”，只拷贝最外层元素，内层嵌套元素则通过引用方式共享，而非独立分配内存
        # 如果需要彻底拷贝则需采用copy.deepcopy()“深拷贝”方式
        # 比如：[1, 2, 3, 4, ['a', 'b', 'c']]
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

    def rotate3(self, nums, k):
        # 思路三
        # 借助外部空间，将后面的元素转移到前面即可。
        k = k % len(nums)
        retote = nums[:len(nums) - k]
        for i in range(len(nums) - k):
            del nums[0]
        nums.extend(retote)


if __name__ == '__main__':
    # case1  res = [5, 6, 7, 1, 2, 3, 4]
    # 解释:
    # 向右旋转 1 步: [7,1,2,3,4,5,6]
    # 向右旋转 2 步: [6,7,1,2,3,4,5]
    # 向右旋转 3 步: [5,6,7,1,2,3,4]
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3

    # case2  res = [3, 99, -1, -100]
    # 解释:
    # 向右旋转 1 步: [99,-1,-100,3]
    # 向右旋转 2 步: [3,99,-1,-100]
    nums2 = [-1, -100, 3, 99]
    k2 = 2

    sol = Solution()
    res1 = sol.rotate1(nums1, k1), sol.rotate2(nums1, k1), sol.rotate3(nums1, k1)
    res2 = sol.rotate1(nums2, k2), sol.rotate2(nums2, k2), sol.rotate3(nums2, k2)
    print('case1:', res1)
    print('case2:', res2)