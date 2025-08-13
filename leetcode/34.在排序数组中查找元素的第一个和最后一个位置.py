#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置

from bisect import bisect_right, bisect_left
# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return [-1, -1]
        right = bisect_right(nums, target) - 1
        left = bisect_left(nums, target)
        return [left, right]
    
            
        
# @lc code=end

