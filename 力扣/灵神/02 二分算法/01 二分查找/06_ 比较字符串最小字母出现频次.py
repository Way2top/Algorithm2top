from bisect import *
# Leetcode:1170
class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        n = len(queries)
        m = len(words)
        words_counts = []
        # 统计 words 中每个单词最小字母出现频次
        for word in words:
            word = sorted(word)
            words_counts.append(bisect_right(word, word[0]))
        words_counts = sorted(words_counts)

        ans = [0] * n
        for i, s in enumerate(queries):
            # 给字符串排序,然后二分法统计最小字母出现的频次
            s = sorted(s)
            count_s = bisect_right(s, s[0])
            ans[i] = m -  bisect_right(words_counts, count_s)
        return ans