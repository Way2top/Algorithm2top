#
# @lc app=leetcode.cn id=2537 lang=python3
#
# [2537] 统计好子数组的数目
#
from collections import defaultdict


# @lc code=start
class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        res = pairs = left = 0
        dic = defaultdict(int)
        for x in nums:
            pairs += dic[x]
            dic[x] += 1
            while pairs >= k:
                dic[nums[left]] -= 1
                pairs -= dic[nums[left]]
                left += 1
            res += left
        return res


# @lc code=end
