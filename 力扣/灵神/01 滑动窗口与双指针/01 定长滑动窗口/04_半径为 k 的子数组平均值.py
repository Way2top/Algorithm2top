# Leetcode：2090
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        if n < 2*k + 1:
            return avgs

        total = sum(nums[:2 * k + 1])
        avgs[k] = total // (2 * k + 1)

        for i in range(1, n - 2 * k):
            total -= nums[i - 1]
            total += nums[i + 2 * k]

            avgs[i + k] = total // (2 * k + 1)

        return avgs


solution = Solution()
ans = solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3)

print(ans)
