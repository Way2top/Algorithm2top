#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = res = 0
        count = 1
        for right, x in enumerate(nums):
            count *= x
            while count >= k:
                count /= nums[left]
                left += 1
            res += right - left + 1
        return res
        
# @lc code=end

