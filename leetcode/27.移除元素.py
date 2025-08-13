#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        
# @lc code=end

