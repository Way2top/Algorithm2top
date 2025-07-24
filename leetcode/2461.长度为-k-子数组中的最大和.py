#
# @lc app=leetcode.cn id=2461 lang=python3
#
# [2461] 长度为 K 子数组中的最大和
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dic = {}
        res = 0
        temp = 0
        
        # 初始化第一个窗口
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            temp += nums[i]
        if len(dic) == k:
            res = temp
        
        # 继续往后遍历
        left = 0
        for right in range(k, n): 
            # 左指针
            dic[nums[left]] -= 1
            temp -= nums[left]
            if dic[nums[left]] == 0:
                del dic[nums[left]]
            left += 1
            
            # 右指针
            dic[nums[right]] = dic.get(nums[right], 0) + 1
            temp += nums[right]
             
            if len(dic) == k:
                res = max(temp, res)
        return res
        
# @lc code=end

