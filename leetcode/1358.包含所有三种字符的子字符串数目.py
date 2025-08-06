#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = res = 0
        dic = {}
        # 当满足条件的时候，就开始移动 left 指针，直至不满足条件，此时内层循环的 [left, right] 这个子串是不满足题目要求的，但是从 0 到 left - 1 都是满足要求的，这样的子数组一共有 left 个，所以 res += left
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
            while len(dic) == 3:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            res += left
        return res
        
        
# @lc code=end

