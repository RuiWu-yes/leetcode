# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 354 俄罗斯套娃信封问题
# @Content : 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
#            当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#            请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# @Explain : 不允许旋转信封。
from bisect import bisect_left  # 二分查找模块


class Solution:
    def maxEnvelopes1(self, envelopes) -> int:
        # 排序+二分法(时间复杂度:O(NlogN), 空间复杂度: O(N))
        # 注意：对数组使用二分搜索，数组一定要是排序数组
        # 按宽度升序排列，如果宽度一样，则按高度降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        def lengthOfLIS(nums):
            top = [1 for _ in range(len(nums))]
            piles = 0  # 牌堆数初始化为0
            for i in range(len(nums)):
                poker = nums[i]  # 要处理的扑克牌
                left, right = 0, piles
                # 搜索左侧边界的二分查找
                while left < right:
                    mid = (left + right) // 2
                    if top[mid] > poker:
                        right = mid
                    elif top[mid] < poker:
                        left = mid + 1
                    else:
                        right = mid
                # 没找到合适的牌堆，新建一堆
                if left == piles:
                    piles += 1
                # 把这张牌放在牌堆顶
                top[left] = poker
            # 牌堆数就是LIS长度
            return piles
        # 根据envelopes的第二维(高度)计算 LIS 的长度就是答案
        return lengthOfLIS([i[1] for i in envelopes])

    def maxEnvelopes2(self, envelopes) -> int:
        # 排序+二分法(时间复杂度:O(NlogN), 空间复杂度: O(N))
        # 使用bisect模块实现二分搜索
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        def lengthOfLIS(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        return lengthOfLIS([i[1] for i in envelopes])


if __name__ == '__main__':
    # case1  res = 3
    # 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]

    sol = Solution()
    res1 = sol.maxEnvelopes1(envelopes)
    res2 = sol.maxEnvelopes2(envelopes)
    print('case1:', res1, res2)