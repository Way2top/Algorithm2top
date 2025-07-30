class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        lo = 0        
        hi = num
        while lo < hi:
            mid = (lo + hi) // 2
            if num < mid ** 2:
                hi = mid
            elif num > mid**2:
                lo = mid + 1
            else:
                return True
        return False