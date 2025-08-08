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
            cnt = defaultdict(int)
            for x in nums:
                pairs += cnt[x]
                cnt[x] += 1
                while pairs >= k:
                    cnt[nums[left]] -= 1
                    pairs -= cnt[nums[left]]
                    left += 1
                res += left
            return res


# @lc code=end
