class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        res = False
        n = len(arr)
        count = 0
        for i in range(n - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                res = True
                return res
        return res
        