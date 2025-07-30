# Leetcode:2389
import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # nums 数组的顺序没有影响，所以先排序
        nums.sort()
        n = len(nums)
        m = len(queries)
        prefix = [0] * (n + 1)

        # 计算前缀和数组
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        ans = [0] * m
        for i in range(m):
            temp =  bisect.bisect_right(prefix, queries[i])
            ans[i] = temp - 1
        
        return ans