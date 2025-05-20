from bisect import *
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for num in arr1: 
            left = bisect_left(arr2, num - d)
            if len(arr2) == left or arr2[left] > num + d:
                ans += 1
        return ans