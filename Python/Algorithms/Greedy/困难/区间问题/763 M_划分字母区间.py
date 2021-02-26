# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 763 划分字母区间
# @Content : 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
#            返回一个表示每个字符串片段的长度的列表。
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 贪心算法
        # 在遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点了。
        # 此时前面出现过所有字母，最远也就到这个边界了。
        # 可以分为如下两步：
        #    1) 统计每一个字符最后出现的位置
        #    2) 从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
        map = {}
        for i in range(len(S)):
            # S[i]为字符，hash[S[i]]为字符出现的最后位置
            map[S[i]] = i
        res = []
        left = right = 0
        for i in range(len(S)):
            right = max(right, map[S[i]])  # 找到字符出现的最远边界
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res


if __name__ == '__main__':
    # case1  res = [9, 7, 8]
    # 解释：
    # 划分结果为 "ababcbaca", "defegde", "hijhklij"。
    # 每个字母最多出现在一个片段中。
    # 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
    S = "ababcbacadefegdehijhklij"

    sol = Solution()
    res = sol.partitionLabels(S)
    print('case1:', res)