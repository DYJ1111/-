class Solution:

    def reverseStr(self, s, k):
        if not s:
            return ""

        chs = list(s)
        for i in range(0, len(chs), 2*k):
            j = min(i+k, len(chs))
            chs[i:j] = reversed(chs[i:j])

        return "".join(chs)