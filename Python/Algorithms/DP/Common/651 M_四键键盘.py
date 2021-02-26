# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 651 四键键盘
# @Content : 假设你有一个特殊的键盘包含下面的按键：
#               Key 1: (A)：在屏幕上打印一个 'A'。
#               Key 2: (Ctrl-A)：选中整个屏幕。
#               Key 3: (Ctrl-C)：复制选中区域到缓冲区。
#               Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
#            现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A’呢？

class Solution:
    def maxA1(self, N: int) -> int:
        # 动态规划:带备忘录的递归解法
        # 时间复杂度:O(N^3), 子问题虽然没有重复了，但数目仍然很多，在LeetCode提交会超时的
        # 对于 (n, a_num, copy) 这个状态，屏幕上能最终最多能有 dp(n, a_num, copy) 个 A
        memo = dict()
        def dp(n, a_num, copy):
            if n <= 0: return a_num;
            # 避免计算重叠子问题
            if (n, a_num, copy) in memo:
                return memo[(n, a_num, copy)]
            memo[(n, a_num, copy)] = max(dp(n - 1, a_num + 1, copy),     # A
                                         dp(n - 1, a_num + copy, copy),  # C-V
                                         dp(n - 2, a_num, a_num))        # C-A C-C
            return memo[(n, a_num, copy)]
        return dp(N, 0, 0)

    def maxA2(self, N: int) -> int:
        # 动态规划
        # 时间复杂度 O(N^2)，空间复杂度 O(N)
        # 定义：dp[i] 表示 i 次操作后最多能显示多少个 A
        dp = [0 for _ in range(N+1)]
        for i in range(1, N+1):
            # 按 A 键
            dp[i] = dp[i-1] + 1
            for j in range(2, i):
                # 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
                # 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        # N 次按键之后最多有几个 A？
        return dp[N]


if __name__ == '__main__':
    # case1  res = 3
    # 解释: 我们最多可以在屏幕上显示三个'A'通过如下顺序按键：A, A, A
    N1 = 3

    # case2  res = 9
    # 解释: 我们最多可以在屏幕上显示九个'A'通过如下顺序按键：A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
    N2 = 7

    sol = Solution()
    res1_1, res1_2 = sol.maxA1(N1), sol.maxA2(N1)
    res2_1, res2_2 = sol.maxA1(N2), sol.maxA2(N2)
    print('case1:', res1_1, res1_2)
    print('case2:', res2_1, res2_2)