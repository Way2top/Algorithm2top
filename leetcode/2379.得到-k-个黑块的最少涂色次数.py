#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count = 0 # 存放连续k个方块中黑色最多的子数组
        # step1: 连续k个方块中黑色最多的子数组
        for i in range(k):
            if blocks[i] == 'B':
                count += 1
        temp = count
        left = 0
        for right in range(k, n):
            if blocks[left] == 'B':
                temp -= 1
            left += 1
            if blocks[right] == 'B':
                temp += 1
            count = max(temp, count)
        
        # step2: 计算其中白色方块的个数
        return k - count
        
# @lc code=end

