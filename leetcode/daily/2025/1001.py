# leetcode:1518

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles -= numExchange - 1
        return res + numBottles

s = Solution()
ans = s.numWaterBottles(15, 4)
print(ans)