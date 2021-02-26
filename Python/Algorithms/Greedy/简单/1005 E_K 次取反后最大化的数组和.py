# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 1005 K 次取反后最大化的数组和
# @Content : 给定一个整数数组 A，我们只能用以下方法修改该数组：
#               我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
#               以这种方式修改数组后，返回数组可能的最大和。


class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        # 贪心算法
        # 局部最优: 让绝对值大的负数变为正数, 当前数值达到最大, 整体最优: 整个数组和达到最大。
        # 局部最优可以推出全局最优。
        # 那么本题的解题步骤为:
        #    第一步: 将数组按照绝对值大小从大到小排序, 注意要按照绝对值的大小
        #    第二步: 从前向后遍历, 遇到负数将其变为正数, 同时K - -
        #    第三步: 如果K还大于0, 那么反复转变数值最小的元素, 将K用完
        #    第四步: 求和
        A.sort(reverse=True, key=lambda x: abs(x))
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1
        if K % 2 == 1:
            A[-1] *= -1
        return sum(A)


if __name__ == '__main__':
    # case1  res = 5
    # 解释：选择索引 (1,) ，然后 A 变为 [4, -2, 3]。
    A1 = [4, 2, 3]
    K1 = 1

    # case2  res = 6
    # 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3, 1, 0, 2]。
    A2 = [3, -1, 0, 2]
    K2 = 3

    # case3  res = 13
    # 解释：选择索引 (1, 4) ，然后 A 变为 [2, 3, -1, 5, 4]。
    A3 = [2, -3, -1, 5, -4]
    K3 = 2

    sol = Solution()
    res1 = sol.largestSumAfterKNegations(A1, K1)
    res2 = sol.largestSumAfterKNegations(A2, K2)
    res3 = sol.largestSumAfterKNegations(A3, K3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)