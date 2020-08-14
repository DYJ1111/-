class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        time: O(n), space: O(1)
        '''
        # 双指针
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums
