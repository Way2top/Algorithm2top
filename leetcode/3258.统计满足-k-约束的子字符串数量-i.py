#
# @lc app=leetcode.cn id=3258 lang=python3
#
# [3258] 统计满足 K 约束的子字符串数量 I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        dic = {'0': 0, '1': 0}
        res = 0
        left = 0
        for right, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
            while dic['0'] > k and dic['1'] > k:
                dic[s[left]] -= 1
                left += 1
            res += right - left + 1
        return res
                
# @lc code=end

