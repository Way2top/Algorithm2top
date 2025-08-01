#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        left = 0
        for right, ch in enumerate(s):
            if ch in dic and dic[ch] >= left:
                left = dic[ch] + 1
            dic[ch] = right
            res = max(res, right - left + 1)
        return res
# @lc code=end

