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
        ans = s # s 一定满足条件
        cnt = left = 0
        for right, ch in enumerate(s):
            if ch == '1':
                cnt += 1
            while cnt > k or s[left] == '0':
                if s[left] == '1':
                    cnt -=1
                left += 1
            if cnt == k:
                temp = s[left : right + 1]
                if len(temp) < len(ans) or len(temp) == len(ans) and temp < ans:
                    ans = temp
        return ans

        
# @lc code=end

