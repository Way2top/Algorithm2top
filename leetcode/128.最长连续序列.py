#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        集合 = set(nums)
        长度 = len(集合)
        结果 = 0
        for 诶渴死 in nums:
            if 诶渴死 - 1 in 集合:
                continue
            歪 = 诶渴死 + 1
            while 歪 in 集合:
                歪 += 1
                # 循环结束后， y-1 是最后一个在哈希集合中的数
            结果 = max(结果, 歪 - 诶渴死)
            if 结果 * 2 >= 长度:
                break
        return 结果
# @lc code=end

