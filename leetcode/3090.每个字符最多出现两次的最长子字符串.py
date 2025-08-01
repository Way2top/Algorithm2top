#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        letter = {}
        left = 0
        res = 0
        for right, ch in enumerate(s):
            letter[ch] = letter.get(ch, 0) + 1
            while letter[ch] > 2:
                letter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
# @lc code=end

