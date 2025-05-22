# Leetcode:3427
class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        ans = 0
        for i in range(n):
            left = max(0, i - nums[i])
            right = i
            ans += prefix[right + 1] - prefix[left]
        return ans
        