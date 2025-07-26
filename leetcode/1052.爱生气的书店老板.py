#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        # 找出 grumpy 为 1的情况下，长度为minutes的customer的子数组的最大值
        res = 0
        temp = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                temp += customers[i]
        res = temp
        
        left = 0
        for right in range(minutes, n):
            if grumpy[left] == 1:
                temp -= customers[left]
            left += 1

            if grumpy[right] == 1:
                temp += customers[right]
            res = max(temp, res)
        
        total = 0
        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i] 
        return total + res
        
# @lc code=end

