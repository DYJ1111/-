class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # import itertools
        # return list(set(itertools.permutations(nums)))
        if not nums:
            return []
        result = set()
        visited = [0] * len(nums)

        def do_permute(nums, track):
            if len(nums) == len(track):
                result.add(tuple(track))
                return

            for i, num in enumerate(nums):
                if visited[i] != 0:
                    continue
                visited[i] = 1
                do_permute(nums, track+[num])
                visited[i] = 0

        do_permute(nums, [])
        return list(result)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # import itertools
        # return list(set(itertools.permutations(nums)))
        if not nums:
            return []
        result = set()

        def do_permute(nums, track):
            if len(nums) == 0:
                result.add(tuple(track))
                return

            for i, num in enumerate(nums):
                do_permute(nums[:i] + nums[i+1:], track+[num])

        do_permute(nums, [])
        return list(result)
