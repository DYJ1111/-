class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        visited = set()

        def permute_core(nums, index, track):
            if index == len(nums):
                result.append(track)
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    permute_core(nums, index+1, track+[num])
                    visited.remove(num)
        permute_core(nums, 0, [])
        return result