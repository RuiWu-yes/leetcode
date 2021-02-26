# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 875 爱吃香蕉的珂珂
# @Content : 珂珂喜欢吃香蕉。这里有N堆香蕉，第 i 堆中有piles[i]根香蕉。警卫已经离开了，将在H小时后回来。
#            珂珂可以决定她吃香蕉的速度K（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。
#            如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
#            珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
#            返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。


class Solution:
    def minEatingSpeed1(self, piles, H: int) -> int:
        # 暴力法
        # piles 数组的最大值
        MAX = max(piles)
        # 注意这个 for 循环，就是在连续的空间线性搜索，这就是二分查找可以发挥作用的标志。
        # 由于我们要求的是最小速度，所以可以用一个搜索左侧边界的二分查找来代替线性搜索，提升效率
        for speed in range(1, MAX):
            # 以 speed 是否能在 H 小时内吃完香蕉
            if self.canFinish(piles, speed, H):
                return speed
        return MAX

    def minEatingSpeed2(self, piles, H: int) -> int:
        # 二分法(搜索左侧边界的二分查找), 算法的时间复杂度为 O(NlogN)
        left, right = 1, max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2  # 防止溢出
            if self.canFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, piles, speed, H):
        time = 0
        for n in piles:
            time += (n // speed) + (1 if n % speed > 0 else 0)
        return time <= H


if __name__ == '__main__':
    # case1  res = 4
    piles1 = [3, 6, 7, 11]
    H1 = 8

    # case2  res = 30
    piles2 = [30, 11, 23, 4, 20]
    H2 = 5

    # case3  res = 23
    piles3 = [30, 11, 23, 4, 20]
    H3 = 6

    sol = Solution()
    res1_1 = sol.minEatingSpeed1(piles1, H1)
    res1_2 = sol.minEatingSpeed2(piles1, H1)
    res2_1 = sol.minEatingSpeed1(piles2, H2)
    res2_2 = sol.minEatingSpeed2(piles2, H2)
    res3_1 = sol.minEatingSpeed1(piles3, H3)
    res3_2 = sol.minEatingSpeed2(piles3, H3)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)
    print('case3:', res3_1, res3_2)