def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    1. 暴力，双循环
    O(n^2)
    """
    """
    method 2
    遍历一次存入hash，再遍历第二次查询 target-num 是否存在于hash
    O(n), O(n)
    """
    dic = {}  # key val: num , index
    for i in range(len(nums)):
        dic[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in dic and dic[target - nums[i]] != i:
            return [i, dic[target - nums[i]]]
    return []
    
    """
    method 3
    一遍 hash，将当前值存入，往后继续遍历，并查看target-num是否存在        
    """
    # dic = {}
    # for i in range(len(nums)):
    #     if (target - nums[i]) not in dic:
    #         dic[nums[i]] = i
    #     else:
    #         return [dic[target - nums[i]], i]
    # return []