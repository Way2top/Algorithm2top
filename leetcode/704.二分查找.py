#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]: 
                return mid
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return -1
# @lc code=end

