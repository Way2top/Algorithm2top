class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        letter = {}
        res = 0
        
        for i in range(n):    
            if s[i] not in letter:
                letter[s[i]] = i
            else:
                index = letter[s[i]]
                letter[s[i]] = i