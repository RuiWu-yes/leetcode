# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 11 盛最多水的容器
# @Content : 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
#            垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#      说明：你不能倾斜容器。
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左右双指针夹逼法
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                # 哪边短，就移动哪边。因为这么移动虽然宽度在缩小，但是有可能遇到的较长的高，此时面积会大于之前的最大面积
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1
        return res


if __name__ == '__main__':
    # case1  res = 49
    # 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # case2  res = 1
    height2 = [1, 1]

    # case3  res = 16
    height3 = [4, 3, 2, 1, 4]

    # case4  res = 2
    height4 = [1, 2, 1]

    sol = Solution()
    res1 = sol.maxArea(height1)
    res2 = sol.maxArea(height2)
    res3 = sol.maxArea(height3)
    res4 = sol.maxArea(height4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)