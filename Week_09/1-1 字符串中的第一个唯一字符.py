class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        dic = {}
        for i, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if dic[ch] and dic[ch] == 1:
                return i
        return -1