# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 45 跳跃游戏 II
# @Content : 给定一个非负整数数组，你最初位于数组的第一个位置。
#            数组中的每个元素代表你在该位置可以跳跃的最大长度。
#            你的目标是使用最少的跳跃次数到达数组的最后一个位置。


class Solution:
    def jump1(self, nums) -> int:
        # 动态规划: 带备忘录的递归解法
        # 该算法的时间复杂度是 递归深度 × 每次递归需要的时间复杂度，即 O(N^2)
        memo = {}
        n = len(nums)
        for i in range(n):
            memo[i] = n
        def dp(nums, p):
            # base case
            if p >= n - 1: return 0
            # 子问题已经计算过
            if memo[p] != n:
                return memo[p]
            steps = nums[p]
            # 你可以选择跳 1 步，2 步...
            for i in range(1, steps+1):
                # 穷举每一个选择
                # 计算每一个子问题的结果
                subProblem = dp(nums, p + i)
                # 取其中最小的作为最终结果
                memo[p] = min(memo[p], subProblem + 1)
            return memo[p]
        return dp(nums, 0)

    def jump2(self, nums) -> int:
        # 贪心算法
        # 动态规划时间复杂度高的根本原因: 需要【递归地】计算出每一个子问题的结果，然后求最值
        # 当前位置元素如果是3,我究竟是跳一步呢,还是两步呢,还是三步呢,究竟跳几步才是最优呢?
        # 其实跳几步无所谓,关键在于可跳的覆盖范围!
        #    不一定非要明确一次究竟跳几步,每次取最大的跳跃步数,这个就是可以跳跃的覆盖范围。
        #    这个范围内,别管是怎么跳的,反正一定可以跳过来。
        # 那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点!
        # 每次移动取最大跳跃步数(得到最大的覆盖范围),每移动一个单位,就更新最大覆盖范围。
        # 贪心选择性质:我们不需要【递归地】计算出所有选择的具体结果然后比较求最值，
        #            而只需要做出那个最有【潜力】，看起来最优的选择即可。
        n = len(nums)
        end, farthest = 0, 0
        jumps = 0
        for i in range(n-1):
            farthest = max(nums[i] + i, farthest)
            if end == i:
                jumps += 1
                end = farthest
        return jumps


if __name__ == '__main__':
    # case1  res = 2
    # 解释: 跳到最后一个位置的最小跳跃数是 2。
    #      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    nums = [2, 3, 1, 1, 4]

    sol = Solution()
    res1 = sol.jump1(nums)
    res2 = sol.jump2(nums)
    print('case1:', res1, res2)