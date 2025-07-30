#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints) 
        # 等价于找到长度为(n - k)的最小子数组
        t =  n - k
        res = 0
        temp = 0
        for i in range(t):
            temp += cardPoints[i]
        res = temp
        left = 0
        for right in range(t, n):
            temp -= cardPoints[left]
            left += 1
            temp += cardPoints[right]
            res = min(res, temp)
        return sum(cardPoints) - res

# @lc code=end

