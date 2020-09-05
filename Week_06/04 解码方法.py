class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        def recursion(index):
            # terminator
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            # process
            sub1 = recursion(index + 1)
            sub2 = 0
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                sub2 = recursion(index + 2)
            return sub1 + sub2

        return recursion(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo = [0] * len(s)

        def recursion(index):
            # terminator
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            # process
            if memo[index] != 0:
                return memo[index]
            res = recursion(index + 1)
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                res += recursion(index + 2)
            memo[index] = res
            return memo[index]

        return recursion(0)