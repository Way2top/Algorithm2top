import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = -math.inf
        min_prefix_sum = prefix_sum = 0
        for x in nums:
            prefix_sum += x
            ans = max(ans, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return ans