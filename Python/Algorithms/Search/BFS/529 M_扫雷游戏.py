# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 529 扫雷游戏
# @Content : 让我们一起来玩扫雷游戏！
#            给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有
#            4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
#            现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
#               1.如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
#               2.如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
#               3.如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
#               4.如果在此次点击中，若无更多方块可被揭露，则返回面板。
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        pass


if __name__ == '__main__':
    # case1
    # 输出：
    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'M', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    board1 = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click1 = [3, 0]

    # case2
    # 输出：
    # [['B', '1', 'E', '1', 'B'],
    #  ['B', '1', 'X', '1', 'B'],
    #  ['B', '1', '1', '1', 'B'],
    #  ['B', 'B', 'B', 'B', 'B']]
    board2 = [['B', '1', 'E', '1', 'B'],
              ['B', '1', 'M', '1', 'B'],
              ['B', '1', '1', '1', 'B'],
              ['B', 'B', 'B', 'B', 'B']]
    click2 = [1, 2]

    sol = Solution()
    res1 = sol.updateBoard(board1, click1)
    res2 = sol.updateBoard(board2, click2)
    print('case1:', res1)
    print('case2:', res2)