# Leetcode:1749
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        res = 0
        prefix = 0
        max_prefix = 0
        min_prefix = 0

        for num in nums:
            prefix += num
            res = max(res, abs(prefix - min_prefix))

            res = max(res, abs(prefix - max_prefix))

            max_prefix = max(max_prefix, prefix)
            min_prefix = min(min_prefix, prefix)

        return res
        