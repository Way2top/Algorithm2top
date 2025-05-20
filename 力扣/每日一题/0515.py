class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)
        ans = [words[0]]
        t = groups[0]
        for i in range(1, n):
            if groups[i] != t:
                ans.append(words[i])
                t = groups[i]
        return ans

s = Solution()
print(s.getLongestSubsequence(["e","a","b"],[0,0,1]))