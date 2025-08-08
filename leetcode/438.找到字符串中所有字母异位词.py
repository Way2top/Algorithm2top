#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_cnt = Counter(p)
        s_cnt = Counter()
        left = 0
        res = []
        for right, ch in enumerate(s):
            s_cnt[ch] += 1
            # 维护窗口长度为 len(p)
            if right >= len(p):
                s_cnt[s[left]] -= 1
                if s_cnt[s[left]] == 0:
                    del s_cnt[s[left]] 
                left += 1
            if p_cnt == s_cnt:
                res.append(left)
        return res
        
# @lc code=end

