# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 268 丢失的数字
# @Content : 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
#       进阶: 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        # 排序(时间复杂度:O(NlogN),空间复杂度:取决于排序算法O(1) 或 O(n))
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num

    def missingNumber2(self, nums: List[int]) -> int:
        # 哈希表(时间复杂度:O(N),空间复杂度:O(N))
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    def missingNumber3(self, nums: List[int]) -> int:
        # 位运算(时间复杂度:O(N),空间复杂度:O(1))
        # 由于异或运算（XOR）满足结合律，并且对一个数进行两次完全相同的异或运算会得到原来的数，因此我们可以通过异或运算找到缺失的数字。
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumber4(self, nums: List[int]) -> int:
        # 数学(时间复杂度:O(N),空间复杂度:O(1))
        # 我们可以用 高斯求和公式 求出 [0..n][0..n] 的和，减去数组中所有数的和，就得到了缺失的数字。高斯求和公式即 n*(n+1)/2
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == '__main__':
    # case1  res = 2
    # 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
    nums1 = [3, 0, 1]

    # case2  res = 2
    # 解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
    nums2 = [0, 1]

    # case3  res = 8
    # 解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    # case4  res = 1
    # 解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
    nums4 = [0]

    sol = Solution()
    res1 = sol.missingNumber1(nums1), sol.missingNumber2(nums1), sol.missingNumber3(nums1), sol.missingNumber4(nums1)
    res2 = sol.missingNumber1(nums2), sol.missingNumber2(nums2), sol.missingNumber3(nums2), sol.missingNumber4(nums2)
    res3 = sol.missingNumber1(nums3), sol.missingNumber2(nums3), sol.missingNumber3(nums3), sol.missingNumber4(nums3)
    res4 = sol.missingNumber1(nums4), sol.missingNumber2(nums4), sol.missingNumber3(nums4), sol.missingNumber4(nums4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)