# Leetcode:125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 提取字符串中的字母和数字
        cleaned = ''.join([ch for ch in s if ch.isalnum()])
        cleaned = cleaned.lower()
        left = 0
        right = len(cleaned) - 1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True

s = Solution()
ans = s.isPalindrome("0P")
print(ans)