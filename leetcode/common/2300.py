import math
from bisect import bisect_right
class Solution:
    # 这里为了巩固一下二分的写法，实际上可以直接使用 python 的 bisect_right
    def upper_bound(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo # lo == hi

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        ans = []
        potions.sort()
        for s in spells:
            target = math.ceil(success / s)
            ans.append(len(potions) - self.upper_bound(potions, target - 1))
        return ans