# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1011 在 D 天内送达包裹的能力
# @Content : 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。传送带上的第 i 个包裹的重量为weights[i]。
#            每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
#            返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。


class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        # 我们要求最小载重，所以可以用搜索左侧边界的二分查找算法优化线性搜索
        left, right = max(weights), sum(weights) + 1  # 载重可能的最小值, 载重可能的最大值 + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, w, D, cap):
        # 如果载重为 cap，是否能在 D 天内运完货物？
        i = 0
        for day in range(0, D):
            maxCap = cap
            while maxCap - w[i] >= 0:
                maxCap -= w[i]
                i += 1
                if i == len(w):
                    return True
        return False


if __name__ == '__main__':
    # case1  res = 15
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D1 = 5

    # case2  res = 6
    weights2 = [3, 2, 2, 4, 1, 4]
    D2 = 3

    # case3  res = 3
    weights3 = [1, 2, 3, 1, 1]
    D3 = 4

    sol = Solution()
    res1 = sol.shipWithinDays(weights1, D1)
    res2 = sol.shipWithinDays(weights2, D2)
    res3 = sol.shipWithinDays(weights3, D3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)