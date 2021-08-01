# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 42 接雨水
# @Content : 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        # 暴力法(时间复杂度O(N^2), 空间复杂度O(1))
        # 对于这种问题，我们不要想整体，而应该去想局部
        #    可以发现这道题的思路其实很简单。具体来说，仅仅对于位置 i，能装下多少水呢？
        n = len(height)
        res = 0
        for i in range(1, n-1):
            l_max, r_max = 0, 0
            # 找右边最高的柱子
            for j in range(i, n):
                r_max = max(r_max, height[j])
            # 找左边最高的柱子
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])
            # 如果自己就是最高的话
            # l_max == r_max == height[i]

            # 位置 i 能达到的水柱高度和其左边的最高柱子、右边的最高柱子有关，
            # 我们分别称这两个柱子高度为 l_max 和 r_max；位置 i 最大的水柱高度就是 min(l_max, r_max)。
            # 更进一步，对于位置 i，能够装的水为：
            res += min(l_max, r_max) - height[i]
        return res

    def trap2(self, height: List[int]) -> int:
        # 暴力法优化(时间复杂度O(N), 空间复杂度O(N))
        # 之前的暴力解法，不是在每个位置 i 都要计算 r_max 和 l_max 吗？
        #    我们直接把结果都提前计算出来，别傻不拉几的每次都遍历，这时间复杂度不就降下来了嘛。
        # 我们开两个数组 r_max 和 l_max 充当备忘录(l_max[i] 表示位置 i 左边最高的柱子高度，r_max[i] 表示位置 i 右边最高的柱子高度)
        # 预先把这两个数组计算好，避免重复计算：
        if not height: return 0
        n = len(height)
        res = 0
        # 数组充当备忘录
        l_max, r_max = [0] * n, [0] * n
        # 初始化
        l_max[0], r_max[-1] = height[0], height[-1]
        # 从左向右计算 l_max
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        # 从右向左计算 r_max
        for i in range(n-2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        # 计算答案
        for i in range(1, n-1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

    def trap3(self, height: List[int]) -> int:
        # 双指针(时间复杂度O(N), 空间复杂度O(1))
        # 这种解法的思路是完全相同的，但在实现手法上非常巧妙，我们这次也不要用备忘录提前计算了，而是用双指针边走边算，节省下空间复杂度。
        #    之前的备忘录解法，l_max[i] 和 r_max[i] 分别代表 height[0..i] 和 height[i..end] 的最高柱子高度。
        #    但是双指针解法中，l_max 和 r_max 代表的是 height[0..left] 和 height[right..end] 的最高柱子高度。
        # 此时的 l_max 是 left 指针左边的最高柱子，但是 r_max 并不一定是 left 指针右边最高的柱子，这真的可以得到正确答案吗？
        #    其实这个问题要这么思考，我们只在乎 min(l_max, r_max)。对于上图的情况，我们已经知道 l_max < r_max 了，
        #    至于这个 r_max 是不是右边最大的，不重要。重要的是 height[i] 能够装的水只和较低的 l_max 之差有关
        if not height: return 0
        n = len(height)
        left, right = 0, n - 1
        res = 0
        l_max, r_max = height[0], height[n - 1]
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    # case1  res = 6
    # 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    # case2  res = 9
    height2 = [4, 2, 0, 3, 2, 5]

    sol = Solution()
    res1 = sol.trap1(height1), sol.trap2(height1), sol.trap3(height1)
    res2 = sol.trap1(height2), sol.trap2(height2), sol.trap3(height2)
    print('case1:', res1)
    print('case2:', res2)