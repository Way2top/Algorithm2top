class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        left = 0
        map = {}
        for right in range(n):
            if s[right] in map:
                left = max(map[s[right], left])
            res = max(res, right - left + 1)
            map[s[right]] = right + 1
        return res