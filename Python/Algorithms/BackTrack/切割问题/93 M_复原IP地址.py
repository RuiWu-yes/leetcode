# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 93 复原IP地址
# @Content : 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#            有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#            例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、
#                 "192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。


class Solution:
    def restoreIpAddresses(self, s: str):
        # 回溯算法
        n = len(s)
        if n < 4 or n > 12:  
            return []
        res = []
        def backtrack(start, track):
            # 如果递归结束，并且track当中刚好存了4个ip
            if start >= n:
                if len(track) == 4:
                    res.append('.'.join(track[:]))
                return
            # 遍历下一个ip是几位
            for end in range(start, min(start + 3, n)):
                # 如果超过1位但是第一位是0，那么非法
                if s[start] == '0' and end > start:
                    return
                # ip必须小于等于255
                if int(s[start: end+1]) > 255:
                    return
                track.append(s[start: end+1])
                backtrack(end+1, track)
                track.pop()
        backtrack(0, [])
        return res


if __name__ == '__main__':
    # case1  res = ["255.255.11.135", "255.255.111.35"]
    s1 = "25525511135"

    # case2  res = ["0.0.0.0"]
    s2 = "0000"

    # case3  res = ["1.1.1.1"]
    s3 = "1111"

    # case4  res = ["0.10.0.10", "0.100.1.0"]
    s4 = "010010"

    # case5  res = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    s5 = "101023"

    sol = Solution()
    res1 = sol.restoreIpAddresses(s1)
    res2 = sol.restoreIpAddresses(s2)
    res3 = sol.restoreIpAddresses(s3)
    res4 = sol.restoreIpAddresses(s4)
    res5 = sol.restoreIpAddresses(s5)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)
    print('case5:', res5)