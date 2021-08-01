# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 448 找到所有数组中消失的数字
# @Content : 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
#            请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
#       进阶: 你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 原地修改(时间复杂度O(N), 空间复杂度O(1))
        # 我们可以用一个哈希表记录数组 nums 中的数字，由于数字范围均在 [1,n] 中，记录数字后我们再利用哈希表检查 [1,n] 中的每一个数是否出现，从而找到缺失的数字。
        # 由于数字范围均在 [1,n] 中，我们也可以用一个长度为 n 的数组来代替哈希表。这一做法的空间复杂度是 O(n) 的。我们的目标是优化空间复杂度到 O(1)。
        # 注意到 nums 的长度恰好也为 n，能否让 nums 充当哈希表呢？
        # 由于 nums 的数字范围均在 [1,n] 中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。
        # 具体来说，遍历 nums，每遇到一个数 x，就让 nums[x−1] 增加 n。由于 nums 中所有数均在 [1,n] 中，增加以后，这些数必然大于 n。
        #         最后我们遍历 nums，若 nums[i] 未大于 n，就说明没有遇到过数 i+1。这样我们就找到了缺失的数字。
        # 注意，当我们遍历到某个位置时，其中的数可能已经被增加过，因此需要对 n 取模来还原出它本来的值。
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        res = [i + 1 for i, num in enumerate(nums) if num <= n]
        return res


if __name__ == '__main__':
    # case1  res = [5, 6]
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]

    # case2  res = [2]
    nums2 = [1, 1]

    sol = Solution()
    res1 = sol.findDisappearedNumbers(nums1)
    res2 = sol.findDisappearedNumbers(nums2)
    print('case1:', res1)
    print('case2:', res2)