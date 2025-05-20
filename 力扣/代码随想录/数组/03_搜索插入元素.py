class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n
        while lo < hi:
            mid = (hi + lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        return hi
