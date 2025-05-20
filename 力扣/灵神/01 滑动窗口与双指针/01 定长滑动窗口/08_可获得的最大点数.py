# Leetcode：1423
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        m = n - k
        opposite_res = 0
        total = 0
        # 初步思路，最后剩下来的一定是一段连续的序列，那么要让拿到手里的最大，也就是让这块剩下来的最小，从而转化为滑动窗口问题
        for i in range(m):
            total += cardPoints[i]
        opposite_res = total

        # 往后滑动
        for i in range(1, n - m + 1):
            total -= cardPoints[i - 1]
            total += cardPoints[i - 1 + m]

            opposite_res = min(opposite_res, total)

        res = sum(cardPoints) - opposite_res
        return res
