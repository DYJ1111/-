class Solution:
    def minPathSum(self, grid):
        """
        傻递归： time: O(2^n), space: O(height)
        """
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        res = [float('inf')]
        def recursion(row, col, temp):
            # terminator
            if row >= m or col >= n:
                return
            if row == m-1 and col == n-1:
                temp += grid[row][col]
                res[0] = min(res[0], temp)
                temp -= grid[row][col]
                return
            # process
            temp += grid[row][col]
            # drill down
            recursion(row + 1, col, temp)
            recursion(row, col+1, temp)
            # reverse state
            temp -= grid[row][col]
        recursion(0, 0, 0)
        return res[0]


class Solution:
    def minPathSum(self, grid):
        """
        记忆化 + 递归： time: O(2^n), space: O(mn)
        """
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        memo = grid
        def recursion(row, col):
            if row == m-1 and col == n-1:
                return memo[row][col]
            if row == m-1:
                return memo[row][col] + recursion(row, col+1)
            if col == n-1:
                return memo[row][col] + recursion(row+1, col)
            return memo[row][col] + min(recursion(row, col+1), recursion(row+1, col))
        return recursion(0, 0)


class Solution:
    def minPathSum(self, grid):
        """
        记忆化 + 迭代： time: O(mn), space: O(mn)
        """
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        memo = grid

        for row in range(1, m):
            for col in range(1, n):
                if row == 0 and col == 0: 
                    continue
                elif row == 0:
                    memo[row][col] += memo[row][col-1]
                elif col == 0:
                    memo[row][col] += memo[row-1][col]
                elif row > 0 and col > 0:
                    memo[row][col] += min(memo[row - 1][col], memo[row][col - 1])

        return memo[m-1][n-1]