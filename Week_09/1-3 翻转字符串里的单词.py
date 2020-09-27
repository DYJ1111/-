logo
探索
题库
圈子
竞赛
面试
职位
商店
2


翻转字符串里的单词
提交记录
25 / 25 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 14.5 MB
提交时间：3 天前
执行用时分布图表
执行消耗内存分布图表
邀请好友来挑战 翻转字符串里的单词
提交的代码： 3 天前
语言： python3


class Solution:
    def reverseWords(self, s):
        if not s:
            return ""

        alist = list(s)
        alist = self.trim_space_headtail(alist)
        alist = self.reverse_string(alist, 0, len(alist)-1)
        alist = self.reverse_word(alist)
        alist = self.trim_space_word(alist)
        return "".join(alist)

    def trim_space_headtail(self, chs):
        i, j = 0, len(chs)-1
        while i <= j and chs[i] == ' ':
            i += 1
        while i <= j and chs[j] == ' ':
            j -= 1
        return chs[i:j+1]

    def reverse_string(self, chs, i, j):
        while i < j:
            chs[i], chs[j] = chs[j], chs[i]
            i += 1
            j -= 1
        return chs

    def reverse_word(self, chs):
        i, j = 0, 0
        while j < len(chs):
            while j < len(chs) and chs[j] != " ":
                j += 1
            self.reverse_string(chs, i, j-1)
            j += 1
            i = j
        return chs

    def trim_space_word(self, chs):
        if not chs:
            return []
        res = [chs[0]]
        for i in range(1, len(chs)):
            if res[-1] == " " and chs[i] == ' ':
                continue
            res.append(chs[i])
        return res
