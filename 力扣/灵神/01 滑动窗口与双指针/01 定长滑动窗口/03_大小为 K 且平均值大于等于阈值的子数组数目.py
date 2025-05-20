# Leetcode：1343
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        res = 0
        n = len(arr)
        total = 0

        for i in range(k):
            total += arr[i]

        if total >= k * threshold:
            res += 1

        for i in range(1, n - k + 1):
            total -= arr[i - 1]
            total += arr[i - 1 + k]
            if total >= k * threshold:
                res += 1
        return res
