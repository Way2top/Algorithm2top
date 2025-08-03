#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # 找出不超过 k 个 0 的最长子数组
        res = 0
        left = 0
        dic = {0: 0, 1: 0}
        for right, digit in enumerate(nums):
            dic[digit] = dic.get(digit, 0) + 1
            while dic[0] > k:
                dic[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
# @lc code=end

