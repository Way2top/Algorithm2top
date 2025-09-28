import math
from math import inf

class Solution:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        res = math.inf
        for i in range(1, n):
            left = nums[:i]
            right = nums[i:]
            if left == list(sorted(left)) and right == list(sorted(right, reverse=True)):
                res = min(res, abs(sum(left) - sum(right)))
        if res == math.inf:
            return -1
        else:
            return res

s = Solution()
res = s.splitArray([3, 1, 2])
print(res)