# Leetcode:34
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if target not in nums:
            return [-1, -1]
        left = self.getLeftBorder(nums, target)
        right = self.getRightBorder(nums, target) - 1
        return [left, right]

    def getRightBorder(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def getLeftBorder(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
