class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # 从前往后遍历，让 nums[i] 处在和下标对应的位置上
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # 排完之后，从前往后遍历
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1