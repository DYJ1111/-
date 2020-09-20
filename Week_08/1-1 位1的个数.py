class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        # 方法1： 会引起死循环
        # time: O(32), space: O(1)
        """
        # while n:
        #     if n & 1:
        #         cnt += 1
        #     n = n >> 1
        # return cnt

        """
        # 方法2：
        # time: O(32), space: O(1)
        """
        # cnt = 0
        # mask = 1
        # for i in range(32):
        #     if n & mask:
        #         cnt += 1
        #     mask = mask << 1
        # return cnt

        """
        # 方法3：n & (n-1) 可以消除 n 最低位的 1
        # time: O(cnt of 1), space: O(1)
        """
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt