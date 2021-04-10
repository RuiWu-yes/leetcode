# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 376 摆动序列
# @Content : 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
#            例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个
#            序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#            给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 贪心算法
        # 局部最优:删除单调坡度上的节点(不包括单调坡度两端的节点),那么这个坡度就可以有两个局部峰值。
        # 整体最优:整个序列有最多的局部峰值,从而达到最⻓摆动序列。
        # 局部最优推出全局最优,并举不出反例,那么试试贪心!
        if len(nums) <= 1: return len(nums)
        preDiff = 0  # 前一对差值
        res = 1  # 记录峰值个数,序列默认序列最右边有一个峰值
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]  # 当前一对差值
            # 出现峰值
            if (curDiff > 0 and preDiff <= 0) or (preDiff >= 0 and curDiff < 0):
                res += 1
                preDiff = curDiff
        return res


if __name__ == '__main__':
    # case1  res = 6
    # 解释: 整个序列均为摆动序列。
    nums1 = [1, 7, 4, 9, 2, 5]

    # case2  res = 7
    # 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
    nums2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]

    # case3  res = 3
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sol = Solution()
    res1 = sol.wiggleMaxLength(nums1)
    res2 = sol.wiggleMaxLength(nums2)
    res3 = sol.wiggleMaxLength(nums3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)