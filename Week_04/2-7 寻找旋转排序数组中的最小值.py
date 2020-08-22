class Solution:
    def findMin(self, nums):
        # 二分查找
        # time: O(logn~n), space: O(1)
        left, right = 0, len(nums)-1
        min_index = left

        while nums[left] >= nums[right]:  # 确认是旋转过的
            if right - left == 1:
                min_index = right
                break
            mid = left + (right - left) // 2
            if nums[mid] == nums[left] == nums[right]:
                return self.linear_search(nums, left, right)
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid

        return nums[min_index]

    def linear_search(self, nums, left, right):
        min_value = nums[left]
        for i, num in enumerate(nums[left+1: right + 1]):
            if min_value > num:
                min_value = num
        return min_value