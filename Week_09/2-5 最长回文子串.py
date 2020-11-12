class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]

        # init all the 1 character palindromes
        for i in range(n):
            dp[i][i] = True

        max_len = 1
        longest_start = 0

        for start in range(n-1, -1, -1):
            for dist in range(1, n-start):
                end = start + dist
                if dist == 1:  # 2 character palindromes
                    dp[start][end] = (s[start] == s[end])
                else:  # >= 3 character palindromes
                    dp[start][end] = (dp[start+1][end-1] and s[start] == s[end])

                if dp[start][end] and end-start+1 > max_len:
                    max_len = end - start + 1
                    longest_start = start
        return s[longest_start: longest_start + max_len]