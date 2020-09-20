class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        集合判重
        """
        # def backtrack(row, path):
        #     if row == n:
        #         paths.append(path[:])
        #         return
        #
        #     for c in range(n):
        #         if c in cols or (row+c) in pie or (row-c) in na:
        #             continue
        #         cols.add(c)
        #         pie.add(row+c)
        #         na.add(row-c)
        #         backtrack(row+1, path + [c])
        #         cols.remove(c)
        #         pie.remove(row+c)
        #         na.remove(row-c)
        #     return
        #
        # cols, pie, na = set(), set(), set()
        # paths = []
        # backtrack(0, [])
        #
        # res = []
        # for temp in paths:
        #     one_res = []
        #     for site in temp:
        #         one_res.append("".join(['Q' if i == site else '.' for i in range(n)]))
        #     res.append(one_res)
        # return res

        """
        二进制位运算判重
        """
        def DFS(row, path, cols, main_diag, sub_diag):
            if row >= n:
                paths.append(path[:])
                return

            bits = (~ (cols | main_diag | sub_diag)) & ((1 << n) - 1)

            while bits:
                cur_one = bits & (-bits)  # 取得最低位的1
                bits = bits & (bits - 1)  # 清零最低位的1
                column = bin(cur_one-1).count('1')  # 统计二进制数中1的个数？？？不明白为何要这一步
                DFS(row+1, path+[column], cols | cur_one, (main_diag | cur_one) >> 1, (sub_diag | cur_one) << 1)
            return

        paths = []
        DFS(0, [], 0, 0, 0)

        res = []
        for temp in paths:
            one_res = []
            for site in temp:
                str_temp = "".join(['Q' if i == site else '.' for i in range(n)])
                one_res.append(str_temp)
            res.append(one_res)
        return res