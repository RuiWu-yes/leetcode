# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 406 根据身高重建队列
# @Content : 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki]
#            表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
#            请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队
#            列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
from typing import List


class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        # 贪心算法(额外 res 数组空间存储)
        # 按照身高从大到小排序后:
        #    局部最优:优先按身高高的people的k来插入。插入操作过后的people满足队列属性
        #    全局最优:最后都做完插入操作，整个队列满足题目队列属性
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            else:
                res.insert(p[1], p)
        return res

    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        # 贪心算法(原地操作)
        people.sort(key=lambda x: (-x[0], x[1]))
        i = 0
        while i < len(people):
            if i > people[i][1]:
                people.insert(people[i][1], people[i])
                people.pop(i + 1)
            i += 1
        return people


if __name__ == '__main__':
    # case1  res = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    # 解释：
    # 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
    # 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
    # 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
    # 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
    # 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
    # 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
    # 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
    people1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    # case2  res = [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    people2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]

    sol = Solution()
    res1 = sol.reconstructQueue1(people1), sol.reconstructQueue2(people1)
    res2 = sol.reconstructQueue1(people2), sol.reconstructQueue2(people2)
    print('case1:', res1)
    print('case2:', res2)