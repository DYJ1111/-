class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # time: O(n), space: O(height) stack
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            # terminator
            if grid[row][col] != '1':
                return
            # process
            grid[row][col] = '#'  # 修改标记
            # drill down
            for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    dfs(x, y)

        lands_cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    lands_cnt += 1
                    dfs(i, j)
        return lands_cnt

        # BFS
        # time: O(n), space: O(n) queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        from collections import deque
        lands_cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.bfs(rows, cols, grid, i, j)
                    lands_cnt += 1
        return lands_cnt

    def bfs(self, rows, cols, grid, i, j):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = '#'  # 1
        while queue:
            # process
            r, c = queue.popleft()
            # grid[r][c] = '#' # 2
            # 错误理解： 1+3 的效果等2
            # 对2的分析：从[0,0]开始，那么[0,1]和[1,0]会入队；然后[0,1]出队，对应[0,2]和[1,1]入队；然后[1,0]出队，对应的[2,0]和[1,1]入队。
            # node adj
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    queue.append((x, y))
                    grid[x][y] = '#'  # 3
        return
