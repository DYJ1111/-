## 1 哈希表、映射、集合

## 2 树、二叉树、二叉搜索树

二叉搜索树：

​	左子树比根节点的值小

​	右子树比根节点的值大

​	其子树依然递归满足以上两点性质

​	**二叉搜索树的中序遍历是升序遍历（做题时必须牢记）**



## 3 堆、二叉堆、图

###  3.1 堆

适用于 top k 问题

有大顶堆和小顶堆

堆有很多实现方式，但在面试中只有二叉堆比较适合

二叉堆使用数组实现，为了方便计算父节点、左右子节点的索引，在初始化时将数组索引为0的位置丢弃不用，由此

以 i 表示当前节点

- parent node : i //2
- left child node : 2 * i
- right child node : 2 * i + 1
- insert 函数：插入到数组尾部，将尾部数值上浮
- delete 函数：将数组尾部的值移动到数组头部，减小数组长度，再将数组头部下沉

### 3.2 图

图的表示方式有两种：

- 邻接矩阵
- 邻接表

基于图的常见算法：

- BFS

  ```python
  def BFS(graph, start, end):
      queue = [start]
      visited = set()
      while queue:
          node = queue.popleft()
          visited.add(node)
          ## 1 process current node
          ...
          ## 2 get related nodes
          nodes = generate_related_nodes(node)  # a function
          queue.append(nodes)
  ```

  

- DFS

```python
visited = set()  # 代码和树最大的区别，原因在于树没有环路，而图可能有环路
def DFS(node, visited):
    if node in visited:  # terminator
        return  # already visited
    
    visited.add(node)
    ## 1 process current node here
    ...
    for nxt_node in node.children():
        if nxt_node not in visited:
            DFS(nxt_node, visited)  # dfs
    
```

