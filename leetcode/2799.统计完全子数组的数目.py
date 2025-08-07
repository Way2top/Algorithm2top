#
# @lc app=leetcode.cn id=2799 lang=python3
#
# [2799] 统计完全子数组的数目
#
from collections import defaultdict
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        kinds = len(set(nums)) # nums 中不同元素的个数
        digit = defaultdict(int)
        left = res = 0
        for right, x in enumerate(nums):
            digit[x] += 1 # 用的是 defaultdict，不需要担心 key 不存在导致报错
            while len(digit) == kinds:
                digit[nums[left]] -= 1
                if digit[nums[left]] == 0:
                    del digit[nums[left]]
                left += 1
            res += left
        return res


# @lc code=end

