# Leetcode：643
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        total = 0
        for i in range(k):
            total += nums[i]
        temp = total
        left = 0
        for right in range(k, n):
            temp -= nums[left]
            left += 1
            temp += nums[right]
            total = max(total, temp)
        return total / k