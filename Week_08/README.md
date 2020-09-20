# 位运算

## 实战要点

（1）判断奇偶  x & 1 == 1 (odd)  x & 1 == 0 (even)

（2）清零最低位的1 x = x & (x-1)

（3）得到最低位的1 x = x & (-x)

（4）x & (~ x) = 0

（5）x >> 1  等于 x // 2

# 布隆过滤器

## 哈希表 vs 布隆过滤器

哈希表：可以判断元素是否在集合中，同时可以存储元素本身和元素到各种额外信息

布隆过滤器：只能判断元素是否在集合中，无法存储额外信息

## 实现、优缺点、应用

一个很长的二进制向量 + 一系列随机映射函数

优点：由于二进制和模糊查询，因此其空间效率和时间效率远超一般算法

缺点：有一定到误识别率，删除困难

总结：查询元素的二进制向量，若存在 0， 则元素肯定不存在

​													若不存在 0，元素可能存在，需要进一步判断

用途：在外层用作快速判断的缓存。当元素可能存在时，进行进一步查找；若元素不存在则停止查找，节省访问数据库的时间

案例：比特币网络、分布式系统（Map-reduce）、Redis缓存、垃圾邮件、评论的过滤

## 代码

```python
from bitarray import bitarray
import mmh3

class BollmFilter(object):
    
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1
    
    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return 'Nope'
        return 'Probably'
```

# LRU Cache

最近最少使用 Least Recently Used

## 实现

大小 + 替换策略

Hash Table + Doubled Linked List  【哈希保证 O(1) 查询，双向队列保证 O(1) 插入删除】

```python
# 调用 API 实现
from collections import OrderedDict

class LRUCache(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key):
        if key not in self.dic.keys():
			return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # update key
        return v
        
    def put(self, key, value):
        if key in self.dic.keys():
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value
        return
    
# Hash Table + Doubled Linked List 实现
class ListNode(object):

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.pre = self.tail, self.head

    def get(self, key):
        if key not in self.dic.keys():
            return -1

        node = self.dic[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val

    def put(self, key, value):
        if key in self.dic.keys():
            self.remove_node(self.dic[key])

        node = ListNode(key, value)
        self.add_node(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            need_remove = self.tail.pre
            self.remove_node(need_remove)  # remove from linkedlist
            del self.dic[need_remove.key]  # remove from dict
        return

    def add_node(self, node):
        # add into head
        nxt = self.head.next
        node.next = nxt
        node.pre = self.head
        self.head.next = nxt.pre = node

    def remove_node(self, node):
        # remove from linked list
        pre = node.pre
        nxt = node.next
        pre.next, nxt.pre = nxt, pre
```

# 排序

## 比较类排序

通过比较决定元素间到相对次序

其时间复杂度不能突破 O(nlogn)，因此也称为 非线性时间比较类排序

* 交换排序：冒泡排序，【快排】
* 插入排序：简单插入，希尔
* 选择排序：简单选择，【堆排】
* 归并排序：二路归并，多路归并

不稳定排序：堆 希尔 快 选

### 代码

```python
def bubble_sort(nums):
    # 交换相邻两个元素，每次都有一个最大的数沉底
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-i):
            if nums[j] <= nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return


def bubble_sort_exch(nums):

    i = 0
    exch = True

    while i < len(nums)-1 and exch:
        exch = False
        for j in range(1, len(nums)-1):
            if nums[j] <= nums[j-1]:
                exch = True
                nums[j-1], nums[j] = nums[j], nums[j-1]
        i += 1
    return


def quick_sort(nums, lo, hi):
    # 分治，递归
    # 每次的privot已经找到正确位置
    # 递归处理privot两侧的数组元素
    if lo >= hi:
        return

    privot = paritation(nums, lo, hi)
    quick_sort(nums, lo, privot-1)
    quick_sort(nums, privot+1, hi)
    return


def paritation(nums, lo, hi):
    privot = hi
    counter = lo

    for i in range(lo, hi):
        if nums[i] < nums[privot]:
            nums[i], nums[counter] = nums[counter], nums[i]
            counter += 1
    nums[counter], nums[hi] = nums[hi], nums[counter]
    return counter


def insertion_sort(nums):
    # 将当前位置的元素插入到已排序数组中正确的位置
    for i in range(1, len(nums)):
        cur_num = nums[i]
        j = i
        while j > 0 and nums[j-1] > cur_num:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = cur_num
    return


def shell_sort(nums):
    # 插入排序是间隔为1的希尔排序，希尔排序是间隔为h的插入排序
    h = 1
    while h < len(nums):
        h = 3 * h + 1

    while h > 0:

        for i in range(h, len(nums)):
            cur_num = nums[i]
            j = i
            while j > 0 and nums[j-h] > cur_num:
                nums[j] = nums[j-h]
                j -= h
            nums[j] = cur_num
        h //= 3
    return


def choice_sort(nums):
    # 每次挑选未排序元素中最小到值放到当前位置
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return


class Min_Heap(object):
    # 插入，删除
    # 使用数组构建堆[build_heap(nums)] or 通过插入操作构建堆[init, insert(k)]

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def build_heap(self, nums):
        self.size = len(nums)
        self.heap = [0] + nums[:]
        i = len(nums) // 2
        while i > 0:
            self.heapify_down(i)
            i -= 1
        return

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.heapify_up(self.size)
        return

    def delete_min(self):
        value = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.heapify_down(1)
        return value

    def heapify_up(self, i):
        while i // 2 > 0:  # 保证i有父节点
            parent = i // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
        return

    def heapify_down(self, i):
        while 2 * i < self.size:  # 保证i有孩子
            min_idx = self.min_child(i)
            if self.heap[i] > self.heap[min_idx]:
                self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            i = min_idx
        return

    def min_child(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            l, r = 2 * i, 2 * i + 1
            if self.heap[l] < self.heap[r]:
                return l
            else:
                return r


def merge_sort(nums, lo, hi):
    if lo >= hi:
        return

    mid = lo + (hi - lo) // 2
    merge_sort(nums, lo, mid)
    merge_sort(nums, mid+1, hi)
    merge(nums, lo, mid, hi)
    return


def merge(nums, lo, mid, hi):
    aux = nums[lo: hi+1]
    i, j = lo, mid + 1
    k = 0
    while i <= mid and j <= hi:
        if nums[i] < nums[j]:
            aux[k] = nums[i]
            i += 1
        else:
            aux[k] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        aux[k] = nums[i]
        i += 1
        k += 1
    while j <= hi:
        aux[k] = nums[j]
        j += 1
        k += 1

    for p in range(k):
        nums[p + lo] = aux[p]
    return


if __name__ == '__main__':
    nums = [1, 3, 52, 25, 25, 48, 48, 56, 98, 74, 2, 3, 25]
    # bubble_sort(nums)
    # bubble_sort_exch(nums)
    # quick_sort(nums, 0, len(nums)-1)
    # insertion_sort(nums)
    # shell_sort(nums)
    # choice_sort(nums)
    # merge_sort(nums, 0, len(nums)-1)
    
    h = Min_Heap()
    h.build_heap(nums)
    print(h.heap)
    for i in range(5):
        print(h.heap[1])
        h.delete_min()
        print(h.heap)
    h.insert(130)
    print(h.heap)
    h.insert(32)
    print(h.heap)
```

## 非比较类排序

不通过比较决定元素到相对次序，可以突破基于比较排序的时间下界，以线性时间运行，因此称为 线性非比较类排序

* 计数排序
* 桶排序
* 基数排序

