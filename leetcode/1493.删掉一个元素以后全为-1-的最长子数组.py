#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # binary array: num
        # condition 1: every element is 1
        n = len(nums)
        if sum(nums) == n:
            return n - 1
        # condition 2: not every element is 1
        # equals to finding the longest subarray containing at least one '0'
        res = 0
        left = 0
        status = 0
        for right in range(n):
            if nums[right] == 0:
                status += 1 
            while status > 1:
                if nums[left] == 0:
                    status -= 1
                left += 1
            res = max(res, right - left) # 'cause the zero must be deleted,the length is not 'left - right + 1'
        return res
        
# @lc code=end

