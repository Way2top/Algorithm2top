# Leetcode：643
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res = float('-inf')
        total = 0
        n = len(nums)

        if n <= k:
            return sum(nums) / n

        for i in range(k):
            total += nums[i]

        res = max(res, total)

        for i in range(1, n - k + 1):
            total -= nums[i - 1]
            total += nums[i - 1 + k]
            res = max(res, total)

        return res / k


solution = Solution()
ans = solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print(ans)
