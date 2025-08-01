#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        # step 1: get the difference between s and t
        diff = []
        for i in range(n):
            diff.append(abs(ord(s[i]) - ord(t[i])))
        # step 2: find the longest subarray whose sum < maxCost
        left = 0
        res = 0
        total = 0
        for right in range(n):
            total += diff[right]
            while total > maxCost:
                total -= diff[left] 
                left += 1
            res = max(res, right - left + 1)
        return res
        
# @lc code=end

