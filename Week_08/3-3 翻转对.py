class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, nums, low, high):
        if low >= high:
            return 0

        mid = low + (high - low) // 2
        ans = self.merge_sort(nums, low, mid) + self.merge_sort(nums, mid+1, high)
        i, j = low, mid + 1
        while i <= mid:
            while j <= high and nums[i]/2 > nums[j]:
                j += 1
            ans += j - (mid + 1)
            i += 1

        self.merge(nums, low, mid, high)
        return ans

    def merge(self, nums, low, mid, high):
        aux = nums[low: high+1]
        i, j = low, mid + 1
        k = 0
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                aux[k] = nums[i]
                i += 1
            else:
                aux[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            aux[k] = nums[i]
            k += 1
            i += 1
        while j <= high:
            aux[k] = nums[j]
            k += 1
            j += 1
        for p in range(len(aux)):
            nums[low + p] = aux[p]
        return