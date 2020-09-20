class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        # 方法1：统计n二进制表示中1的个数，如果只有1个1，return True, 否则 False
        # time: O(32), space: O(1)
        # 方法2： 位运算：2的幂次方二进制表示中只存在一个1，故 n&(n-1) 的结果为0
        # time: O(1), space: O(1)
        """
        if not n:
            return False

        if not n & (n-1):
            return True
        return False