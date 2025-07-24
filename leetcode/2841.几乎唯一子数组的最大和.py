#
# @lc app=leetcode.cn id=2841 lang=python3
#
# [2841] 几乎唯一子数组的最大和
#

# @lc code=start
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        n = len(nums)
        res = 0
        temp = 0
        # 长度为 k 的子数组中，不同元素的个数大于等于 m，求和
        letter = {}
        for i in range(k): 
            letter[nums[i]] = letter.get(nums[i], 0) + 1
            temp += nums[i]
        if len(letter) >= m:
            res = temp
        
        left = 0
        for right in range(k, n):
            # 左指针
            letter[nums[left]] -= 1
            temp -= nums[left]
            if letter[nums[left]] == 0:
                del letter[nums[left]]
            left += 1

            # 右指针
            letter[nums[right]] = letter.get(nums[right], 0) + 1
            temp += nums[right]

            if len(letter) >= m:
                res = max(temp, res)
        return res

s = Solution()
ans = s.maxSum([2,6,7,3,1,7], 3, 4)
print(ans)
# @lc code=end

