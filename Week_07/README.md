# 知识点

## 字典树 Trie

### 应用

用于统计和排序大量的字符串（但不仅限于字符串），例如搜索引擎用于文本词频统计

### 优点

查询效率高，减少了无谓的字符串比较

### 基本性质

1 根节点不包含字符，除根节点外的每个节点都只包含一个字符，节点本身不存在完整单词

2 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串

3 每个节点的所有子节点路径代表的字符串都不相同

### 核心思想

1 空间换时间

2 利用字符串的公共前缀来降低查询时间的开销，以达到提高效率的目的

### 代码模板

```python
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

## 并查集 Disjoint Set

### 适用场景

组团，配对问题。例如朋友圈的个数

### 基本操作

makeSet(s): 建立一个并查集，其中包含 s 个单元素集合 【init】

unionSet(x, y): 把元素 x 和元素 y 所在的集合合并，要求 x 和 y 不相交。如果相交则不合并 【union】

find(x): 找到元素 x 所在的集合的代表，该操作也可用于判断两个元素是否位于同一个集合，只要比较两个元素所处集合的代表是否一致即可 【parent】

### 代码模板

```python
self.count = 0  # 统计集合的数量
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)]
	self.count = len(p)
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	if p1 == p2:
		return
	p[p1] = p2
	self.count -= 1 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root:  # 找到代表元素
        root = p[root] 
	while p[i] != i: # 路径压缩: 将路径上经过的所有元素都直接指向代表元素
        x = i
        i = p[i]
        p[x] = root 
	return root
```



# 作业

## 简单

爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）

## 中等

实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）
朋友圈（亚马逊、Facebook、字节跳动在半年内面试中考过）
岛屿数量（近半年内，亚马逊在面试中考查此题达到 361 次）
被围绕的区域（亚马逊、eBay、谷歌在半年内面试中考过）
有效的数独（亚马逊、苹果、微软在半年内面试中考过）
括号生成（亚马逊、Facebook、字节跳动在半年内面试中考过）
单词接龙（亚马逊、Facebook、谷歌在半年内面试中考过）
最小基因变化（谷歌、Twitter、腾讯在半年内面试中考过）

## 困难

单词搜索 II （亚马逊、微软、苹果在半年内面试中考过）
N 皇后（亚马逊、苹果、字节跳动在半年内面试中考过）
解数独（亚马逊、华为、微软在半年内面试中考过）