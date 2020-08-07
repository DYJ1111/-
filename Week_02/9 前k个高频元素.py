def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    前k个最小元素，大顶堆
    前k个最大元素，小顶堆
    """
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    import heapq
    max_heap = [(-val, key) for key, val in dic.items()]  # 需要大顶堆，因此使用-val
    heapq.heapify(max_heap)  # 构建小顶堆
    res = []
    for _ in range(k):
        # pop 出来的 结构 (-val, key), we need key to return
        res.append(heapq.heappop(max_heap)[1])  
    return res