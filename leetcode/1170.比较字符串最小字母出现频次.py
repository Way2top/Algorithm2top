#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#
from bisect import bisect_right
# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        n = len(queries)
        m = len(words)
        words_cnt = []
        res = [0] * n
        for w in words:
            w = sorted(w)
            words_cnt.append(bisect_right(w, w[0]))
        words_cnt = sorted(words_cnt)

        for i, q in enumerate(queries):
            q = sorted(q)
            q_cnt = bisect_right(q, q[0])
            res[i] = m - bisect_right(words_cnt, q_cnt)
        return res
# @lc code=end

