class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心
        # time: O(nlogn) n 是 g 或 s 中较长的 , space: O(1)
        kids = sorted(g)
        foods = sorted(s)

        i, j = 0, 0
        children = 0
        while i < len(kids) and j < len(foods):
            if kids[i] <= foods[j]:
                children += 1
                i += 1
            j += 1
        return children