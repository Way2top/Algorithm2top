#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#


# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        # equivalent to finding the longest subarray which all elements appear less than k times.
        left = 0
        res = 0
        dic = {}
        for right, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            while dic[num] > k:
                dic[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# @lc code=end
