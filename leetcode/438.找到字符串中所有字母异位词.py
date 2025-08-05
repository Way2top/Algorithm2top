#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from collections import Counter
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_counter = Counter(p)
        window = Counter()
        left = right = 0
        res = []
        while right < len(s):
            window[s[right]] += 1
            if right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if right - left + 1 == len(p) and p_counter == window:
                res.append(left)
            right += 1
        return res
# @lc code=end

