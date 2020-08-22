## 深度优先搜索和广度优先搜索

1. 属于暴力搜索（一般会伴随相关剪枝操作）
2. 要确保树中或图中每个节点访问一次且仅访问一次！！！
    （1）对于 bfs 和 dfs 来说，可以使用 集合或者哈希 保存已经遍历过的节点，避免重复遍历
    （2）对于 bfs 来说，有时可以为了降低空间复杂度，可以改变图的节点状态，避免重复遍历
            使用这种方法时，在刚加入节点时，就要改变其状态，否则可能会出现**重复入队**的情况！！！

```python
# DFS-递归
visited = set()
def dfs(node)
	if node in visited:
        return
    # process
    visited.add(node)
    ...
    # drill down
    for nxt in node.children:
        if nxt not in visited:
            dfs(nxt)
	return

# DFS-栈
visited = set()
def dfs_stack(node):
    if not node:
        return
    
    stack = [node]
    while stack:
        v = stack.pop()
        visited.add(v)
        # process node
        ...
        # push into stack
        for nxt in v.next:
            if nxt not in visited:
                stack.append(nxt)
        # other work to do
	return

# BFS-哈希
visited = set()
def bfs(graph, start, end):
    queue = [start]
    while queue:
        node = queue.popleft()
        visited.add(node)
        # process
        ...
       	for adj in node.adjs:
            if adj not in visited:
	            queue.append(adj)
    return

# BFS-改变状态
def bfs(graph, i, j):
    queue = [(i, j)]
    graph[i][j] = '#'
    while queue:
        r, c = queue.popleft()
        # process
        ...
       	for x, y in [...]:
            if graph[x][y]满足条件:
	            queue.append(adj)
                graph[x][y] = '#'
    return
```

### 实战题目

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description

https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description

https://leetcode-cn.com/problems/generate-parentheses/#/description

https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/#/description

### 课后作业

https://leetcode-cn.com/problems/word-ladder/description/

https://leetcode-cn.com/problems/word-ladder-ii/description/

https://leetcode-cn.com/problems/number-of-islands/

https://leetcode-cn.com/problems/minesweeper/description/

------



## 贪心

对每个子问题当下做局部最优判断，不能回退

### 课后作业

https://leetcode-cn.com/problems/lemonade-change/description/

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/

https://leetcode-cn.com/problems/assign-cookies/description/

https://leetcode-cn.com/problems/walking-robot-simulation/description/

https://leetcode-cn.com/problems/jump-game/

https://leetcode-cn.com/problems/jump-game-ii/

------



## 二分查找

条件：  

1. 目标函数具有单调性
2. 存在上下界
3. 能够通过索引访问

```python
def binary_search(alist, target):
    left, right = 0, len(alist)-1  ## 
    
    while left <= right:  ## 
        mid = left + (right - left) // 2
        if alist[mid] == target:
            return res
        elif alist[mid] < target:
            left = mid + 1
        elif alist[mid] > target:
            right = mid - 1
            
    return -1
```

具体问题

一般会有**旋转数组，但数组部分有序**，依然可以使用二分查找
可以将 **mid 跟 left** 的值进行对比

当 mid > left 时，说明 left ~ mid 有序
	然后判断 target 是否处于 left ~ mid 之间，否则就在另外一边
	
当 mid < left 时，说明 mid ~ right 有序
	判断 target 是否处于 mid ~ right 之间，否则就在另外一边

### 实战题目

https://leetcode-cn.com/problems/sqrtx/

https://leetcode-cn.com/problems/valid-perfect-square/

### 课后作业

https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

https://leetcode-cn.com/problems/search-a-2d-matrix/

https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

    可以将 **mid 跟 left** 的值进行对比

    当 mid > left 时，说明 left ~ mid 有序
        mid ~ right 无序
        
    当 mid < left 时，说明 mid ~ right 有序
        left ~ mid 无序

