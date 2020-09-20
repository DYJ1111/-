class Solution:
    def totalNQueens(self, n):
        """
        方法1： 集合判重
        """
        # self.cnt = 0
        #
        # def backtrack(row):
        #     if row == n:
        #         self.cnt += 1
        #         return
        #
        #     for c in range(n):
        #         if c in cols or (row+c) in pie or (row-c) in na:
        #             continue
        #         cols.add(c)
        #         pie.add(row+c)  # sub_diagonal 副对角线： 行下标 + 列下标
        #         na.add(row-c)   # main_diagonal 主对角线， 行下标 - 列下标
        #         backtrack(row+1)
        #         cols.remove(c)
        #         pie.remove(row+c)
        #         na.remove(row-c)
        #     return
        #
        # cols, pie, na = set(), set(), set()
        # backtrack(0)
        # return self.cnt

        """
        方法2： 二进制判重
        """
        if n <= 0:
            return []
        self.cnt = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.cnt

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.cnt += 1
            return

        # cols | pie | na 保存的是不能放置皇后的位置
        # ~ (cols | pie | na) 保存的是可以放置皇后的位置
        # x & ((1 << n) - 1) 将 x 最高位至第n位清零
        bits = (~(cols | pie | na)) & ((1 << n) - 1)

        while bits:
            # 先取得最低位的1进行递归； 再清零最低位的1；便于递归下一个1在二进制中的位置
            p = bits & (-bits)  # 取得最低位的1
            bits = bits & (bits - 1)  # 清除最低位的1
            # cols | p 表示 列 不能放置皇后的位置
            # (pie | p) << 1 表示 副对角线(sub_diagonal) 不能放置皇后的位置
            # (na | p) >> 1 表示 主对角线(main_diagonal) 不能放置皇后的位置
            self.DFS(n, row+1, cols | p, (pie | p) << 1, (na | p) >> 1)
        return