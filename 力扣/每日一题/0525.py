# Leetcode:2131
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        n = len(words)
        dic = {}
        res = 0
        for ch in words:
            if ch[0] == ch[1]:
                res += 2
             
            
        for val in dic.values():
            if val % 2 == 0:
                res += val * 2
            else:
                res += (val - 1) * 2
        return res
        