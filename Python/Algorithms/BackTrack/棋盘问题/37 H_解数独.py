# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 37 解数独
# @Content : 编写一个程序，通过填充空格来解决数独问题。
#            一个数独的解法需遵循如下规则：
#            数字 1-9 在每一行只能出现一次。
#            数字 1-9 在每一列只能出现一次。
#            数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#            空白格用 '.' 表示。
#      提示 :
#            1) 给定的数独序列只包含数字 1-9 和字符 '.' 。
#            2) 你可以假设给定的数独只有唯一解。
#            3) 给定数独永远是 9x9 形式的。


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 算法的核心思路非常非常的简单，就是对每一个空着的格子穷举 1 到 9，
        #    1) 如果遇到不合法的数字（在同一行或同一列或同一个 3×3 的区域中存在相同的数字）则跳过，
        #    2) 如果找到一个合法的数字，则继续穷举下一个空格子。
        self.backtrack(board, 0, 0)

    def backtrack(self, board, i, j):
        m = n = 9
        if j == n:
            # 穷举到最后一列的话就换到下一行重新开始
            return self.backtrack(board, i + 1, 0)
        if i == m:
            # 找到一个可行解，触发 base case
            return True
        if board[i][j] != '.':
            # 如果有预设数字，不用我们穷举
            return self.backtrack(board, i, j + 1)
        for s in range(1, 10):
            ch = str(s)
            # 如果遇到不合法的数字，就跳过
            if not self.isVaild(board, i, j, ch):
                continue
            board[i][j] = ch
            # 如果找到一个可行解，立即结束
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = '.'
        # 穷举完 1-9，依然没有找到可行解，此路不通
        return False

    def isVaild(self, board, r, c, n):
        for i in range(9):
            # 判断行是否存在重复
            if board[r][i] == n: return False
            # 判断列是否存在重复
            if board[i][c] == n: return False
            # 判断 3 x 3 方框是否存在重复
            if board[(r//3)*3 + i//3][(c//3*3 + i%3)] == n: return False
        return True


if __name__ == '__main__':
    # case1
    # 输出：
    # [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    #  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    #  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    #  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    #  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    #  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    #  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    #  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    #  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    sol = Solution()
    sol.solveSudoku(board)
    print(board)