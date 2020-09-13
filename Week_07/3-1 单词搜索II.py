class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        纯回溯法：
        time： O(len(words)*m*n*4^n)
        space: O(len(word))

        Time limit exceeded
        """

        def backtrack(row, col, word, index, visited):
            # terminator
            if not 0 <= row < m or not 0 <= col < n or board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            # process
            visited.add((row, col))
            # drill down
            for x, y in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if (x, y) not in visited:
                    if backtrack(x, y, word, index+1, visited):
                        return True
            # reverse state if needed
            visited.remove((row, col))
            return False

        if not board or len(board[0]) == 0:
            return []

        res = set()
        m, n = len(board), len(board[0])
        for item in words:
            for r in range(m):
                for c in range(n):
                    visited = set()
                    if backtrack(r, c, item, 0, visited):
                        res.add(item)
        return list(res)


# 字典树 + DFS
class Trie:

    def __init__(self):
        self.root = {}
        self.is_word = '#'

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.is_word] = self.is_word


class Solution:
    """
    字典树 + DFS
    time: O(m*n*4^n)
    space: O(m*n)
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def backtrack(row, col, node, path):
            # terminator
            if trie.is_word in node:
                res.add(path)  # 有可能只是字符串前缀，需要继续向下查找
            if not 0 <= row < m or not 0 <= col < n or (row, col) in visited or board[row][col] not in node:
                return
            # process
            visited.add((row, col))
            # drill down
            for x, y in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                backtrack(x, y, node[board[row][col]], path + board[row][col])
            # reverse states
            visited.remove((row, col))
            return

        # === code here ===
        if not board or len(board) == 0 or len(board[0]) == 0:
            return []
        # 根据 words 构建 Trie树
        trie = Trie()
        for word in words:
            trie.insert(word)
        # 搜索
        res = set()
        m, n = len(board), len(board[0])
        node = trie.root
        visited = set()
        for r in range(m):
            for c in range(n):
                backtrack(r, c, node, "")
        return list(res)