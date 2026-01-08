class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) # 左闭右开的写法
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1 # 正因为是左闭右开，所以 mid 已经判断过了，因此 left 应该从 mid + 1 开始判断
            else:
                right = mid # 以为是左闭右开，mid 已经判断过了，因此应该从 mid - 1 开始判断，因此 right = mid（右开）
        return left
        