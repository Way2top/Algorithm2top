# Leetcode：1456
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowel = ('a', 'e', 'i', 'o', 'u')
        left = 0
        right = k - 1 
        res = 0
        for i in range(k):
            if s[i] in vowel:
                res += 1
        temp = res
        for right in range(k, n):
            if s[left] in vowel:
                temp -= 1
            left += 1
            if s[right] in vowel:
                temp += 1
            res = max(res, temp)
        return res

s = Solution()
res = s.maxVowels("abciiidef", 3)
print(res)