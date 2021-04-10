# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 239 滑动窗口最大值
# @Content : 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
#            滑动窗口每次只向右移动一位。
#            返回滑动窗口中的最大值。
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 队列(先入先出)
        res, queue = [], []
        for i in range(len(nums)):
            if not queue:  # 如果为空直接加入队列
                queue.append(i)
            else:
                if i == queue[0] + k:  # 如果队首的索引已位于滑动窗口之外，将其出队
                    queue.pop(0)
                while queue and nums[queue[-1]] < nums[i]:  # 将小于当前值的队尾元素依次出队
                    queue.pop()
                queue.append(i)  # 将当前值加入队列
            res.append(nums[queue[0]])  # 队首即最大值
        return res[k-1:]  # k-1前不是有效的滑动窗口


if __name__ == '__main__':
    # case1  res = [3, 3, 5, 5, 6, 7]
    # 解释：
    # 滑动窗口的位置                   最大值
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    #  1 [3  -1  -3] 5  3  6  7       3
    #  1  3 [-1  -3  5] 3  6  7       5
    #  1  3  -1 [-3  5  3] 6  7       5
    #  1  3  -1  -3 [5  3  6] 7       6
    #  1  3  -1  -3  5 [3  6  7]      7
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3

    # case2  res = [1]
    nums2 = [1]
    k2 = 1

    # case3  res = [1, -1]
    nums3 = [1, -1]
    k3 = 1

    # case4  res = [11]
    nums4 = [9, 11]
    k4 = 2

    # case5  res = [4]
    nums5 = [4, -2]
    k5 = 2

    sol = Solution()
    res1 = sol.maxSlidingWindow(nums1, k1)
    res2 = sol.maxSlidingWindow(nums2, k2)
    res3 = sol.maxSlidingWindow(nums3, k3)
    res4 = sol.maxSlidingWindow(nums4, k4)
    res5 = sol.maxSlidingWindow(nums5, k5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)