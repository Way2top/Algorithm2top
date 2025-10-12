class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = {}
        res = left = temp = 0
        for right, ch in enumerate(s):
            letter[ch] = letter.get(ch, 0) + 1
            temp += 1 
            while letter[ch] > 1:
                letter[s[left]] -= 1
                left += 1
                temp -= 1
            res = max(temp, res)
        return res
