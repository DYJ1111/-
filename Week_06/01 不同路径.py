class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        傻递归： time O(2^n), space O(height)递归树的高度
        """
        if m <= 0 or n <= 0:
            return 0

        def path(row, col):
            # terminator
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            # process and drill down
            down = path(row+1, col)
            right = path(row, col+1)
            return down + right

        return path(0, 0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        记忆化 + 递归： time: O(m*n), space: O(m*n)
        """
        if m <= 0 or n <= 0:
            return 0
        memo = [[0] * n for _ in range(m)]

        def path(row, col):
            # terminator
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            # process and drill down
            if memo[row][col] == 0:
                memo[row][col] = path(row+1, col) + path(row, col+1)
            return memo[row][col]

        return path(0, 0)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        记忆化 + 迭代： time: O(m*n), space: O(m*n)
        """
        if m <= 0 or n <= 0:
            return 0
        memo = [[0] * n for _ in range(m)]

        for i in range(m):
            memo[i][n-1] = 1
        for i in range(n):
            memo[m-1][i] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                memo[i][j] = memo[i+1][j] + memo[i][j+1]

        return memo[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        记忆化 + 迭代： time: O(m * n), space: O(2n)
        """
        if m <= 0 or n <= 0:
            return 0
        
        bottom = [1] * n
        cur = [1] * n
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cur[j] = cur[j+1] + bottom[j]
            bottom, cur = cur, bottom
        return bottom[0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        记忆化 + 迭代： time: O(m * n), space: O(n)
        """
        if m <= 0 or n <= 0:
            return 0

        cur = [1] * n

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cur[j] += cur[j+1]
        return cur[0]