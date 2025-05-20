# 力扣：2563
from typing import List
from bisect import bisect


def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    res = 0
    for i in range(len(nums)):
        left = bisect(nums, lower - nums[i] - 1, i + 1)
        right = bisect(nums, upper - nums[i], i + 1) - 1
        res += right - left + 1

    return res
