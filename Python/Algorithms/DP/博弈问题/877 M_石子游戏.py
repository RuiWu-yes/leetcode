# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 877 石子游戏
# @Content : 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
#            游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
#            亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
#            这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。假设亚历克斯和
#            李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。


class Solution:
    # 博弈类问题的套路都差不多，其核心思路是在二维 dp 的基础上使用元组分别存储两个人的博弈结果。
    # 掌握了这个技巧以后，别人再问你什么俩海盗分宝石，俩人拿硬币的问题，你就告诉别人：我懒得想，直接给你写个算法算一下得了。

    # 我们「石头游戏」改的更具有一般性：
    #    你和你的朋友面前有一排石头堆，用一个数组 piles 表示，piles[i] 表示第 i 堆石子有多少个。你们轮流拿石头，一次拿一堆，但是只能拿走最左边
    # 或者最右边的石头堆。所有石头被拿完后，谁拥有的石头多，谁获胜。
    #    石头的堆数可以是任意正整数，石头的总数也可以是任意正整数，这样就能打破先手必胜的局面了。比如有三堆石头 piles = [1, 100, 3]，先手不管
    # 拿 1 还是 3，能够决定胜负的 100 都会被后手拿走，后手会获胜。
    #    假设两人都很聪明，请你设计一个算法，返回先手和后手的最后得分（石头总数）之差。比如上面那个例子，先手能获得 4 分，后手会获得 100 分，你
    # 的算法应该返回 -96。
    # 这样推广之后，这个问题算是一道 Hard 的动态规划问题了。博弈问题的难点在于，两个人要轮流进行选择，而且都贼精明，应该如何编程表示这个过程呢？
    def stoneGame(self, piles) -> bool:
        # 动态规划
        # dp[i][j]的定义：
        #   dp[i][j][0] 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数。
        #   dp[i][j][1] 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数。
        # 状态转移方程: 根据前面对 dp 数组的定义，状态显然有三个：(1) 开始的索引 i (2) 结束的索引 j (3) 当前轮到的人
        #             对于这个问题的每个状态，可以做的选择有两个：选择最左边的那堆石头，或者选择最右边的那堆石头。
        #             这道题的难点在于，两人是交替进行选择的，也就是说先手的选择会对后手有影响，这怎么表达出来呢？
        #             根据我们对 dp 数组的定义，很容易解决这个难点，写出状态转移方程：
        #                 dp[i][j][0] = max(piles[i] + dp[i + 1][j][1], piles[j] + dp[i][j - 1][1])
        #                 dp[i][j][0] = max(选择最左边的石头堆, 选择最右边的石头堆)
        #                解释：我作为先手，面对 piles[i...j] 时，有两种选择：
        #                   要么我选择最左边的那一堆石头，然后面对 piles[i+1...j]
        #                   但是此时轮到对方，相当于我变成了后手；
        #                   要么我选择最右边的那一堆石头，然后面对 piles[i...j-1]
        #                   但是此时轮到对方，相当于我变成了后手。
        #
        #                 if 先手选择左边:
        #                     dp[i][j][1] = dp[i + 1][j][0]
        #                 if 先手选择右边:
        #                     dp[i][j][1] = dp[i][j - 1][0]
        #                解释：我作为后手，要等先手先选择，有两种情况：
        #                   如果先手选择了最左边那堆，给我剩下了 piles[i+1...j]
        #                   此时轮到我，我变成了先手；
        #                   如果先手选择了最右边那堆，给我剩下了 piles[i...j-1]
        #                   此时轮到我，我变成了先手。
        n = len(piles)
        # 初始化 dp 数组
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # 填入 base case
        for i in range(n):
            dp[i][i][0] = piles[i]
        # 遍历需要一定技巧，保证列方向从左往右，行方向从下往上填表
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 先手选择最左边或最右边的分数
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                # 套用状态转移方程
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        res = dp[0][n - 1]
        return res[0] > res[1]


if __name__ == '__main__':
    # case1  res = true
    # 解释：
    # 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
    # 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
    # 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
    # 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
    # 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
    piles = [5, 3, 4, 5]

    sol = Solution()
    res = sol.stoneGame(piles)
    print('case1:', res)