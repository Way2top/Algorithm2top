#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        target = max(nums)
        left = cnt = 0
        res = 0
        for x in nums:
            if x == target:
                cnt += 1
            while cnt == k:
                if nums[left] == target:
                    cnt -= 1
                left += 1
            res += left
        return res
            

        
# @lc code=end

