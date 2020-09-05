class Solution:
    def minimumTotal(self, triangle):
        """
        递归：  time: O(2^n), space: O(height)
        """
        if not triangle or len(triangle[0]) == 0:
            return 0

        def recursion(level, col):
            if level+1 == len(triangle):
                return triangle[level][col]

            left = recursion(level+1, col)
            right = recursion(level+1, col+1)
            return min(left, right) + triangle[level][col]

        return recursion(0, 0)


class Solution:
    def minimumTotal(self, triangle):
        """
        记忆化 + 递归： time: O(mn), space: O(mn)
        """
        if not triangle or len(triangle[0]) == 0:
            return 0
        memo = [[0] * len(row) for row in triangle]

        def recursion(level, col):
            if level+1 == len(triangle):
                return triangle[level][col]
            if memo[level][col] != 0:
                return memo[level][col]

            left = recursion(level+1, col)
            right = recursion(level+1, col+1)
            memo[level][col] = min(left, right) + triangle[level][col]
            return memo[level][col]

        return recursion(0, 0)


class Solution:
    def minimumTotal(self, triangle):
        """
        记忆化 + 迭代： time: O(mn), space: O(mn)
        """
        if not triangle or len(triangle[0]) == 0:
            return 0

        memo = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                memo[i][j] += min(memo[i+1][j], memo[i+1][j+1])

        return memo[0]


class Solution:
    def minimumTotal(self, triangle):
        """
        记忆化 + 迭代： time: O(mn), space: O(n)
        """
        if not triangle or len(triangle[0]) == 0:
            return 0

        memo = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                memo[j] = min(memo[j], memo[j+1]) + triangle[i][j]

        return memo[0]