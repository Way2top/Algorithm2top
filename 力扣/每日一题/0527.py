# Leetcode:2894
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = (1 + n) * n / 2
        sum2 = (m + m*(n//m))*(n//m) / 2
        return int(sum1 - sum2*2)