# Leetcode:69
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        lo = 0
        hi = x
        ans = 0        
        while lo < hi:
            mid = (lo + hi) // 2
            if x < mid*mid:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1