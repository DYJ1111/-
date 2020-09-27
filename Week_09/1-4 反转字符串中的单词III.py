class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""

        # strs = list(s)
        # i, j = 0, 0
        # while j < len(strs):
        #     while j < len(strs) and strs[j] != ' ':
        #         j += 1
        #     m, n = i, j - 1
        #     while m < n:
        #         strs[m], strs[n] = strs[n], strs[m]
        #         m += 1
        #         n -= 1
        #     j += 1
        #     i = j
        # return "".join(strs)
        return " ".join([word[::-1] for word in s.split()])