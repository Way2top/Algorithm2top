#
# @lc app=leetcode.cn id=2904 lang=python3
#
# [2904] 最短且字典序最小的美丽子字符串
#

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        count = left = 0
        ans = s
        for right, ch in enumerate(s):
            count += int(ch)
            while count > k or s[left] == '0':
                count -= int(s[left])
                left += 1
            if count == k:
                temp = s[left : right + 1]
                if len(temp) < len(ans) or len(temp) == len(ans) and temp < ans:
                    ans = temp
        return ans
        
# @lc code=end

