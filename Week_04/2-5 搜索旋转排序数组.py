class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        # time: O(logn), space: O(1)
        if not nums: return -1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:  # left sorted
                # in ascending order side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right sorted
                # in ascending order side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1