class Solution:
    def upper_bound(self, nums, target) -> int:
        lo, hi = 0, len(nums) 
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo # lo == hi
        
    def maximumCount(self, nums: list[int]) -> int:
        pos = self.upper_bound(nums, -1)
        neg = len(nums) - self.upper_bound(nums, 0)
        return max(pos, neg)
        