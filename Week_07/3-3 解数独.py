class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack():
            if not need_fill:
                return True
            r, c = need_fill[0]
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if num not in row[r] and num not in col[c] and num not in square[r//3][c//3]:
                    # process
                    need_fill.popleft()
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    square[r//3][c//3].add(num)
                    # drill down
                    if backtrack():
                        return True
                    # reverse states
                    row[r].remove(num)
                    col[c].remove(num)
                    square[r // 3][c // 3].remove(num)
                    need_fill.appendleft((r, c))
                    board[r][c] = '.'

            return False

        if not board:
            return
        # set
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        from collections import deque
        need_fill = deque()  # 记录需要填充的位置
        # init set
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    need_fill.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[i//3][j//3].add(board[i][j])
        # fill
        backtrack()
        return
