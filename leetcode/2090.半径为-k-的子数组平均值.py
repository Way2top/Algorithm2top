#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        if 2*k + 1 > n:
            return avgs
        ans = 0
        for i in range(2*k + 1):
            ans += nums[i]
        avgs[k] = ans // (2*k + 1)
        left = 0
        for right in range(k + 1, n - k):
            ans -= nums[left]
            left += 1
            ans += nums[2*k + left]
            avgs[right] = ans // (2*k + 1)
        return avgs

        
s = Solution()
# 37 32 34
ans = s.getAverages([7,4,3,9,1,8,5,2,6], 3)
print(ans)
        
# @lc code=end

