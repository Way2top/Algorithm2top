#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        # equivalent to finding the sum of longest subarray without duplicate elements
        left = 0
        res = temp = 0
        dic = {}
        for right, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            temp += num
            while dic[num] > 1:
                dic[nums[left]] -= 1
                temp -= nums[left]
                left += 1
            res = max(res, temp)
        return res
        
# @lc code=end

