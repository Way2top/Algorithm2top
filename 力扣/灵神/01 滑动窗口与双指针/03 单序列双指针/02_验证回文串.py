# Leetcode:125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将字符串中的给字母数字字符删除
        res = s
        for ch in s:
            if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 132):