#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = {}
        res = 0
        left = 0
        for right, ch in enumerate(s):
            letter[ch] = letter.get(ch, 0) + 1
            while letter[ch] > 1:
                letter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res
# @lc code=end

