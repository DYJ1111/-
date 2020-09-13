class Solution:
    """
    并查集
    time: O(n^3)
    space: O(n)
    """
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        def disjoint_set(n):
            p = [i for i in range(n)]
            self.count = len(p)
            return p

        def find(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i
                i = p[i]
                p[x] = root
            return root

        def union(i, j):
            p1 = find(i)
            p2 = find(j)
            if p1 == p2:
                return
            p[p1] = p2
            self.count -= 1

        self.count = 0
        p = disjoint_set(len(M))
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1 and i != j:
                    union(i, j)

        return self.count


class Solution:
    """
    DFS
    time: O(n^2)
    space: o(n)
    """
    def findCircleNum(self, M):
        if not M:
            return 0

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in range(N):
                if M[i][j] == 1:
                    dfs(j)
            return

        N = len(M)
        count = 0
        visited = set()
        for i in range(N):
            if i not in visited:
                dfs(i)
                count += 1
        return count


class Solution:
    """
    BFS
    time: O(n^2)
    space: O(n)
    """
    def findCircleNum(self, M):
        if not M:
            return 0

        N = len(M)
        count = 0
        visited = set()
        from collections import deque
        queue = deque()
        for i in range(N):
            if i not in visited:
                queue.append(i)
                count += 1
                while queue:
                    tmp = queue.popleft()
                    visited.add(tmp)
                    for j in range(N):
                        if M[tmp][j] == 1 and j not in visited:
                            queue.append(j)

        return count