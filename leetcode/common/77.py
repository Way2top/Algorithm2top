class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if n < k:
            return [[]]
        res = []
        def getTotalCombine(start: int, k):
            if start >= n:
                return
            curr = []
            for i in range(start + 1, n):
                curr.append([start, ])

