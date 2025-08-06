#
# @lc app=leetcode.cn id=3325 lang=python3
#
# [3325] 字符至少出现 K 次的子字符串 I
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = left = 0
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
            while dic[ch] == k:
                dic[s[left]] -= 1
                left += 1
            res += left
        return res

s = Solution()
ans = s.numberOfSubstrings('abcde', 1)
# @lc code=end

