class Solution:
    def searchMatrix(self, matrix, target):
        # 二分查找
        # time: O(n), space: O(1)
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols-1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1

        return False