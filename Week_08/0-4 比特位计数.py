class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        # 方法1： 每个 n 单独统计，再加入到 res
        # time: O(nk), k是n中1的个数，space: O(1)
        """
        # def count(n):
        #     cnt = 0
        #     while n:
        #         cnt += 1
        #         n = n & (n-1)
        #     return cnt
        #
        # res = []
        # for i in range(num+1):
        #     res.append(count(i))
        # return res

        """
        # 方法2： DP
        # time: O(n), space: O(1),存储结果的空间不算
        """
        dp = [0] * (num + 1)
        for i in range(1, num+1):
            dp[i] = dp[i & (i-1)] + 1

        return dp