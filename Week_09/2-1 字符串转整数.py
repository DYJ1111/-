class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0 or len(str.strip()) == 0:
            return 0

        str = list(str.strip())
        sign = -1 if str[0] == '-' else 1
        if str[0] in ['-', '+']: 
            del str[0]

        res = 0
        for ch in str:
            if ch.isdigit():
                res = res*10 + (ord(ch) - ord('0'))
            else:
                break

        return max(-2**31, min(sign * res, 2**31-1))