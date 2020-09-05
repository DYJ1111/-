class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        记忆化 + 迭代： time: O(mn), space: O(mn)
        """
        if not obstacleGrid or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]

        # 当在最后一行或最后一列遇到了一个障碍物，则前面无法通过
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                break
            memo[i][n-1] = 1
        for i in range(n-1, -1, -1):
            if obstacleGrid[m-1][i] == 1:
                break
            memo[m-1][i] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    memo[i][j] = memo[i+1][j] + memo[i][j+1]
        return memo[0][0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        记忆化 + 迭代： time: O(mn), space: O(n)
        """
        if not obstacleGrid or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * n
        for i in range(n-1, -1, -1):
            if obstacleGrid[m-1][i] == 1:
                break
            cur[i] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif j < n-1:
                    cur[j] += cur[j+1]
        return cur[0]