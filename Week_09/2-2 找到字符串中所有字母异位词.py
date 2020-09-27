class Solution:
    def findAnagrams(self, s, p):
        if not s:
            return []

        res = []
        # length_of_p = len(p)
        # refer = sorted(p)
        # for i in range(len(s) - len(p) + 1):
        #     sub_str = sorted(s[i:i+length_of_p])
        #     if refer == sub_str:
        #         res.append(i)
        #
        # return res
        chars = [0] * 26

        for ch in p:
            chars[ord(ch) - ord('a')] += 1

        left, right = 0, 0
        cnt = len(p)

        while right < len(s):

            if chars[ord(s[right]) - ord('a')] >= 1:
                cnt -= 1
            chars[ord(s[right]) - ord('a')] -= 1
            right += 1

            if right - left == len(p):
                if cnt == 0:
                    res.append(left)

                if chars[ord(s[left]) - ord('a')] >= 0:
                    cnt += 1
                chars[ord(s[left]) - ord('a')] += 1
                left += 1

        return res