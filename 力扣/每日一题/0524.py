class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans = []
        for i, ch in enumerate(words):
            if x in ch:
                ans.append(i)
        return ans
        