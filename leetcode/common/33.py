class Solution:
    def search(self, nums: list[int], target: int) -> int:
        end = nums[-1]
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            
            # 如果 nums[mid] 和 target 不在一边
            if nums[mid] > end and target <= end:
                lo = mid + 1
            elif nums[mid] <= end and target > end:
                hi = mid
            # 在同一边，正常二分
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return -1
        