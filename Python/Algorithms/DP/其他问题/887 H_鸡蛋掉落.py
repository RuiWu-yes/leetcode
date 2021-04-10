# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 887 鸡蛋掉落
# @Content : 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N 共有 N 层楼的建筑。每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。你知
#            道存在楼层 F ，满足 0 <= F <= N 任何从高于 F的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。每次移动，你可以
#            取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。你的目标是确切地知道 F 的值是多少
#            无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？


class Solution:
    def superEggDrop1(self, K: int, N: int) -> int:
        # 动态规划1:带备忘录的递归解法 O(K*N^2)
        memo = {}
        def dp(K, N):
            # base case
            if K == 1: return N
            if N == 0: return 0
            # 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            # 穷举所有可能的选择
            for i in range(1, N+1):
                res = min(
                          res,
                          max(dp(K, N - i), dp(K - 1, i - 1)) + 1
                         )
            # 记入备忘录
            memo[(K, N)] = res
            return res
        return dp(K, N)

    def superEggDrop2(self, K: int, N: int) -> int:
        # 动态规划2:dp数组的迭代解法 O(K*N^2)
        # 状态方程：dp[i, j] 最多用j个蛋， 扔i次， 到底最多能测量多高？
        # 状态拆解：你第一次扔蛋，选这栋楼中间一层（那个点就是后面的 + 1）
        #         如果碎了，测的次数少1，蛋少1，dp[i - 1][j - 1] 在楼的下半部分
        #         如果没碎，测的次数少1，这个蛋还能接着用，dp[i - 1][j] 在楼的上半部分
        #         那总长度 = 上 + 1 + 下
        # 何时返回：如果 dp[i][K] >= N 了， 说明我用了K个蛋，扔了i次，最多能测出N层，那i就是答案
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 + dp[i - 1][j]
                if dp[i][K] >= N:
                    return i

    def superEggDrop3(self, K: int, N: int) -> int:
        # 动态规划3:二分法进行优化 O(K*N*logN)
        memo = dict()
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(K, N)] = res
            return res
        return dp(K, N)


if __name__ == '__main__':
    # # case1  res = 2
    # 鸡蛋从 1 楼掉落.如果它碎了,我们肯定知道 F = 0.
    # 否则,鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1.
    # 如果它没碎,那么我们肯定知道 F = 2.
    # 因此,在最坏的情况下我们需要移动 2 次以确定 F 是多少.
    K1 = 1
    N1 = 2

    # case2  res = 3
    K2 = 2
    N2 = 6

    # case3  res = 4
    K3 = 3
    N3 = 14

    sol = Solution()
    res1 = sol.superEggDrop1(K1, N1), sol.superEggDrop2(K1, N1), sol.superEggDrop3(K1, N1)
    res2 = sol.superEggDrop1(K2, N2), sol.superEggDrop2(K2, N2), sol.superEggDrop3(K2, N2)
    res3 = sol.superEggDrop1(K3, N3), sol.superEggDrop2(K3, N3), sol.superEggDrop3(K3, N3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)