class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        O(T):O(N),O(s):O(1)
        """
        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j+1