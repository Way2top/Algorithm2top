import bisect
class Solution:
    def lower_bound(self, nums, target) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.lower_bound(nums, target)
        right = self.lower_bound(nums, target + 1) - 1
        if left == len(nums):
            return [-1, -1]
        return [left, right]