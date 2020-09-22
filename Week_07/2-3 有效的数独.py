class Solution:
    def isValidSudoku(self, board):
        """
        time: O(1), space: O(1)
        """
        if not board:
            return True

        # # row
        # for r in range(9):
        #     row_used = [False] * 10
        #     for c in range(9):
        #         if board[r][c] != '.':
        #             num = int(board[r][c])
        #             if row_used[num]:
        #                 return False
        #             row_used[num] = True
        #
        # # col
        # for c in range(9):
        #     col_used = [False] * 10
        #     for r in range(9):
        #         if board[r][c] != '.':
        #             num = int(board[r][c])
        #             if col_used[num]:
        #                 return False
        #             col_used[num] = True
        #
        # #  box
        # for i, j in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
        #     box_used = [False] * 10
        #     for r in range(3):
        #         for c in range(3):
        #             if board[i*3 + r][j*3 + c] != '.':
        #                 num = int(board[i*3 + r][j*3 + c])
        #                 if box_used[num]:
        #                     return False
        #                 box_used[num] = True

        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        box = [[False] * 10 for _ in range(9)]

        for i in range(9):  # row
            for j in range(9):  # col
                if board[i][j] != '.':
                    number = ord(board[i][j]) - ord('0')
                    if row[i][number] or col[j][number] or box[j//3 + (i//3)*3][number]:
                        return False

                    row[i][number] = True
                    col[j][number] = True
                    # j // 3 表示前3行的不同box， (i//3)表示在第几个3行的box， 再乘以3表示在第几个3行的第几个box
                    box[j//3 + (i//3) * 3][number] = True

        return True