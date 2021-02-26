# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 773 滑动谜题
# @Content : 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#            一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#            最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#            给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。


class Solution:
    def slidingPuzzle(self, board) -> int:
        m , n = 2, 3
        start = ''
        target = '123450'
        # 将 2x3 的数组转化成字符串
        for i in range(m):
            for j in range(n):
                start += (str(board[i][j]) + '0')
        # 记录一维字符串的相邻索引
        neighbor = [
            {1, 3},
            {0, 4, 2},
            {1, 5},
            {0, 4},
            {3, 1, 5},
            {4, 2}
        ]

        # BFS算法框架
        queue = [start]
        visited = {start}
        step = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                # 判断是否达到目标局面
                if target == cur:
                    return step
                # 找到数字0的索引
                idx = 0
                for s in cur:
                    if s != '0':
                        idx += 1
                # 将数字0和相邻数字交换位置
                for adj in neighbor[idx]:
                    new_board = cur
                    new_board[adj], new_board[idx] = new_board[idx], new_board[adj]
                    # 防止走回头路
                    if new_board not in visited:
                        queue.append(new_board)
                        visited.add(new_board)
            step += 1
        return -1


if __name__ == '__main__':
    # case1  res = 1
    # 解释：交换 0 和 5 ，1 步完成
    board1 = [[1, 2, 3], [4, 0, 5]]

    # case2  res = -1
    # 解释：没有办法完成谜板
    board2 = [[1, 2, 3], [5, 4, 0]]

    # case3  res = 5
    # 解释：
    # 最少完成谜板的最少移动次数是 5 ，
    # 一种移动路径:
    # 尚未移动: [[4,1,2],[5,0,3]]
    # 移动 1 次: [[4,1,2],[0,5,3]]
    # 移动 2 次: [[0,1,2],[4,5,3]]
    # 移动 3 次: [[1,0,2],[4,5,3]]
    # 移动 4 次: [[1,2,0],[4,5,3]]
    # 移动 5 次: [[1,2,3],[4,5,0]]
    board3 = [[4, 1, 2], [5, 0, 3]]

    sol = Solution()
    res1 = sol.slidingPuzzle(board1)
    res2 = sol.slidingPuzzle(board2)
    res3 = sol.slidingPuzzle(board3)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)