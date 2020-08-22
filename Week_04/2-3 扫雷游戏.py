class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # dfs
        # time: O(board), space: O(stack)
        if not board or len(board[0]) == 0:
            return []

        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            elif board[r][c] == 'E':
                cnt = 0
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
                            (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'M':
                        cnt += 1
                if cnt == 0:
                    board[r][c] = 'B'
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),
                                 (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)]:
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'E':
                            dfs(x, y)
                else:
                    board[r][c] = str(cnt)

        dfs(click[0], click[1])
        return board