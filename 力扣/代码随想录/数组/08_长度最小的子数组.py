# Leetcode:209
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        res = n
        left = 0
        count = 0
        for right in range(n):
            ans += nums[right]
            while ans >= target:
                res = min(res, right - left + 1)
                ans -= nums[left]
                left += 1
                count += 1
        if count == 0:
            return 0
        return res

s = Solution()
print(s.minSubArrayLen(15, [1,2,3,4,5]))