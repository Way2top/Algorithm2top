class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        dic = {}
        for right, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
            while dic[ch] > 1:
                dic[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans