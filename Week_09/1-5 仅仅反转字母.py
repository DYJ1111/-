class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return ""

        # strs = list(S)
        # i, j = 0, len(strs)-1
        # while i < j:
        #     while i < j and not strs[i].isalpha():
        #         i += 1
        #     while i < j and not strs[j].isalpha():
        #         j -= 1
        #     strs[i], strs[j] = strs[j], strs[i]
        #     i += 1
        #     j -= 1
        # return "".join(strs)

        from collections import deque
        stack = deque()
        for ch in S:
            if ch.isalpha():
                stack.append(ch)

        res = ""
        for ch in S:
            if ch.isalpha():
                res += stack.pop()
            else:
                res += ch
        return res