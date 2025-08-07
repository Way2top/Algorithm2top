#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        length = cnt = res = left = 0
        for right, x in enumerate(nums):
            length += 1
            cnt += x
            while length * cnt >= k:
                cnt -= nums[left]
                length -= 1
                left += 1
            res += right - left + 1
        return res

        
# @lc code=end

