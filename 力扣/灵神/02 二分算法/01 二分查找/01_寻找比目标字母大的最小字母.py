# Leetcode:744
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        lo = 0
        hi = len(letters)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < letters[mid]:
                hi = mid
            else:
                lo = mid + 1
        return letters[lo]
        