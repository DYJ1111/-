

## 刷题误区： 只刷一遍

## 核心： 升维 +  空间换时间



## 知识点：

数组 array 的解题技巧：快慢指针、左右指针（左右夹逼）

​	lookup: O(1)

​	insert / delete: O(n)

链表 linked list 的解题技巧：快慢指针，ps：熟能生巧

​	循环链表： tail.next = head

​	lookup: O(n)

​	insert / delete: O(1)

​	工程应用 LRU Cache

跳表 skip list 对应于 AVL 和 二分查找

​	insert / delete/ lookup: O(logN)

​	空间复杂度： 是各级新增加的 节点数

​	工程应用 Redis

栈 stack 适用于 最近相关性 问题， 可以根据 最近相关性 判断题目是否可以使用 栈 来解答

​	入栈 / 出栈: O(1)

​	search: O(n)

队列 queue 适用于 先来后到 顺序的问题

​	入队 / 出队： O(1)

​	search: O(n)

双端队列 deque  的应用： 滑动窗口

​	insert / delete: O(1)

​	search: O(n)

优先级队列 Priority queue 的底层实现有多种，比较熟悉的例如： 堆

​	insert: O(1)  ??? 有点迷惑

​	按元素优先级取出： O(logN)



## 问题： 

（1）开始使用五毒神掌，感觉有些题目的代码直接背下来了，在重复刷题的时候思维没有动，这个后期会不会改善？

（2）关于 LRU Cache，是哪种数据结构的工程应用（linked list or queue）？