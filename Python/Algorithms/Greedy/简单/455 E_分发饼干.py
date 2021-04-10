      # -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 455 分发饼干
# @Content : 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
#            对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块
#            饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，
#            这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心算法
        # 局部最优：小饼干喂给胃口小的,充分利用饼干尺寸喂饱一个
        # 全局最优：喂饱尽可能多的小孩。
        g.sort()
        s.sort()
        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1
        return index


if __name__ == '__main__':
    # case1  res = 1
    # 解释:
    # 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
    # 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
    # 所以你应该输出1。
    g1 = [1, 2, 3]
    s1 = [1, 1]

    # case2  res = 2
    # 解释:
    # 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
    # 你拥有的饼干数量和尺寸都足以让所有孩子满足。
    # 所以你应该输出2.
    g2 = [1, 2]
    s2 = [1, 2, 3]

    sol = Solution()
    res1 = sol.findContentChildren(g1, s1)
    res2 = sol.findContentChildren(g2, s2)
    print('case1:', res1)
    print('case2:', res2)