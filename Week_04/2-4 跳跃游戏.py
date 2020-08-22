class Solution:
    def canJump(self, nums):
        # 贪心
        # time: O(n), space: O(1)
        max_dis = 0

        for i, num in enumerate(nums):  # i 为当前位置，num为可跳距离
            if max_dis < i: return False
            max_dis = max(max_dis, i + num)
        return True