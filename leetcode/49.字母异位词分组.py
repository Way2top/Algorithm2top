#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        return list(res.values())
        
# @lc code=end

