# Leetcode：1343
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        target = k * threshold
        total = 0
        left = 0
        res = 0
        for i in range(k):
            total += arr[i]

        if total >= target:
            res += 1
            
        for right in range(k, n):
            total -= arr[left]
            left += 1
            total += arr[right]
            if total >= target:
                res += 1
        return res

s = Solution()
ans = s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)
print(ans)