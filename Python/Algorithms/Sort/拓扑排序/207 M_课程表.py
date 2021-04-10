# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 207 课程表
# @Content : 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#            在选修某些课程之前需要一些先修课程。例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#            给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # 拓扑排序
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses


if __name__ == '__main__':
    # case1  res = true
    # 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
    numCourses1, prerequisites1 = 2, [[1, 0]]

    # case2  res = false
    # 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成 课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
    numCourses2, prerequisites2 = 2, [[1, 0], [0, 1]]
    sol = Solution()
    res1 = sol.canFinish(numCourses1, prerequisites1)
    res2 = sol.canFinish(numCourses2, prerequisites2)
    print('case1:', res1)
    print('case2:', res2)