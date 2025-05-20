# Leetcode:3355
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        # 求出 nums 的前缀和数组
        prefix = [0] * n
        for i in range(nums):
            if i == 0:
                prefix[i] = nums[i]
            prefix[i] = prefix[i - 1] + nums[i]
        
        