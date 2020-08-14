

## 刷题误区： 只刷一遍

## 核心： 升维 +  空间换时间



# 知识点

## 数组 array 

​	解题技巧：快慢指针、左右指针（左右夹逼）

​	lookup: O(1)

​	insert / delete: O(n)

## 链表 linked list 

​	解题技巧：快慢指针，ps：熟能生巧

​	循环链表： tail.next = head

​	lookup: O(n)

​	insert / delete: O(1)

​	工程应用 LRU Cache

## 跳表 skip list 

​	对应于 AVL 和 二分查找

​	insert / delete/ lookup: O(logN)

​	空间复杂度： 是各级新增加的 节点数

​	工程应用 Redis

## 栈 stack 

​	适用于 最近相关性 问题， 可以根据 最近相关性 判断题目是否可以使用 栈 来解答

​	入栈 / 出栈: O(1)

​	search: O(n)

## 队列 queue 

​	适用于 先来后到 顺序的问题

​	入队 / 出队： O(1)

​	search: O(n)

## 双端队列 deque  

​	应用： 滑动窗口

​	insert / delete: O(1)

​	search: O(n)

## 优先级队列 Priority queue 的

​	其底层实现有多种，比较熟悉的例如： 堆

​	insert: O(1)  ??? 有点迷惑

​	按元素优先级取出： O(logN)



## 问题

（1）开始使用五毒神掌，感觉有些题目的代码直接背下来了，在重复刷题的时候思维没有动，这个后期会不会改善？

（2）关于 LRU Cache，是哪种数据结构的工程应用（linked list or queue）？



# Week 01  算法题

    Week01
    【day1】  爬楼梯 https://github.com/a4471174/algorithm013/blob/master/Week_01/ClimbStairs.java
    【day2】  加一   https://github.com/a4471174/algorithm013/blob/master/Week_01/PlusOne.java
    【day3】  两数之和 https://github.com/a4471174/algorithm013/blob/master/Week_01/TwoSum.java
    【day4】  两两交换链表中的节点 https://github.com/a4471174/algorithm013/blob/master/Week_01/SwapPairs.java
    【day5】  合并两个有序链表 https://github.com/a4471174/algorithm013/blob/master/Week_01/MergeTwoLists.java
    【day6】  猜数字游戏 https://github.com/a4471174/algorithm013/blob/master/Week_01/GetHint.java   
    【day7】  设计循环双端队列 https://github.com/a4471174/algorithm013/blob/master/Week_01/MyCircularDeque.java


##   实战题目 - Array

    1. https://leetcode-cn.com/problems/container-with-most-water/              @TODO
    2. https://leetcode-cn.com/problems/move-zeroes/                            @TODO
    3. https://leetcode-cn.com/problems/climbing-stairs/                        @UNDERWAY  1 time
    4. https://leetcode-cn.com/problems/3sum/ (高频老题）                        @TODO

##   实战练习题目 - Linked List

    1. https://leetcode-cn.com/problems/reverse-linked-list/                    @TODO
    2. https://leetcode-cn.com/problems/swap-nodes-in-pairs                     @UNDERWAY  1 time
    3. https://leetcode-cn.com/problems/linked-list-cycle                       @TODO
    4. https://leetcode-cn.com/problems/linked-list-cycle-ii                    @TODO
    5. https://leetcode-cn.com/problems/reverse-nodes-in-k-group/               @TODO    

##   homework

    1. https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/    @TODO
    2. https://leetcode-cn.com/problems/rotate-array/                           @TODO
    3. https://leetcode-cn.com/problems/merge-two-sorted-lists/                 @UNDERWAY  1 time
    4. https://leetcode-cn.com/problems/merge-sorted-array/                     @TODO
    5. https://leetcode-cn.com/problems/two-sum/                                @UNDERWAY  1 time
    6. https://leetcode-cn.com/problems/move-zeroes/                            @TODO
    7. https://leetcode-cn.com/problems/plus-one/                               @UNDERWAY  1 time

##   实战题目

    1. https://leetcode-cn.com/problems/largest-rectangle-in-histogram          @TODO
    2. https://leetcode-cn.com/problems/sliding-window-maximum                  @TODO

##   homework    

    1. https://leetcode.com/problems/design-circular-deque                      @UNDERWAY  1 time
    2. https://leetcode.com/problems/trapping-rain-water/                       @TODO

