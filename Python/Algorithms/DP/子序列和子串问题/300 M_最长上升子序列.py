# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 300 最长上升子序列
# @Content : 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# @explain : 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
#            你算法的时间复杂度应该为 O(n2)。
#      进阶 : 你能将算法的时间复杂度降低到 O(n log n) 吗?


class Solution:
    def lengthOfLIS1(self, nums) -> int:
        # 动态规划 O(N2)
        if not nums: return 0
        # dp数组应该全部初始化为1，因为子序列最少也要包含自己，所以长度最小为1
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 既然是递增子序列，我们只要找到前面那些结尾比nums[i]小的子序列，然后把nums[i]接到最后，就可以形成一个新的递增子序列，而且这个新的子序列长度加一
                    # 子序列可能有很多，我们只要最长的那个
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums) -> int:
        # 二分查找 O(NlogN)
        # 参考耐心纸牌游戏规则:
        #    1) 只能把点数小的牌压到点数比它大的牌上。
        #    2) 如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去。
        #    3) 如果当前牌有多个堆可供选择，则选择最左边的堆放置。
        #    为什么遇到多个可选择堆的时候要放到最左边的堆上呢？因为这样可以保证牌堆顶的牌有序, 以至于可以用二分查找降低搜索难度
        top = [0 for _ in range(len(nums))]
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


if __name__ == '__main__':
    # case1  res = 4
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    sol = Solution()
    res1 = sol.lengthOfLIS1(nums)
    res2 = sol.lengthOfLIS2(nums)
    print(res1)
    print(res2)