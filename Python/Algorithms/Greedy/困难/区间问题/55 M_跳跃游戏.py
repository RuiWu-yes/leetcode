# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 55 跳跃游戏
# @Content : 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#            数组中的每个元素代表你在该位置可以跳跃的最大长度。
#            判断你是否能够到达最后一个下标。


class Solution:
    def canJump(self, nums) -> bool:
        # 贪心算法
        # 当前位置元素如果是3,我究竟是跳一步呢,还是两步呢,还是三步呢,究竟跳几步才是最优呢?
        # 其实跳几步无所谓,关键在于可跳的覆盖范围!
        #    不一定非要明确一次究竟跳几步,每次取最大的跳跃步数,这个就是可以跳跃的覆盖范围。
        #    这个范围内,别管是怎么跳的,反正一定可以跳过来。
        # 那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点!
        # 每一步都计算一下从当前位置最远能够跳到哪里，然后和一个全局最优的最远位置 farthest 做对比，
        # 通过每一步的最优解，更新全局最优解，这就是贪心。
        n = len(nums)
        farthest = 0
        for i in range(n-1):
            # 不断计算能跳到的最远距离
            farthest = max(farthest, i + nums[i])
            # 可能碰到了 0，卡住跳不动了
            if farthest <= i: return False
        return farthest >= n-1


if __name__ == '__main__':
    # case1  res = true
    # 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
    nums1 = [2, 3, 1, 1, 4]

    # case2  res = false
    # 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
    nums2 = [3, 2, 1, 0, 4]

    sol = Solution()
    res1 = sol.canJump(nums1)
    res2 = sol.canJump(nums2)
    print('case1:', res1)
    print('case2:', res2)