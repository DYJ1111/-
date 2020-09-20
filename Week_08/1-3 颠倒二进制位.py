class Solution:
    def reverseBits(self, n: int) -> int:
        """
        # 将 二进制表示中每一位单独取出来，再左移到目标位置
        """

        res = 0
        move = 31
        while n:
            res += (n & 1) << move
            n = n >> 1
            move -= 1
        return res