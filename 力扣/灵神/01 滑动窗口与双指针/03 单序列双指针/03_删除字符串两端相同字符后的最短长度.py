# Leetcode:1750
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[right]
            # 左边往后找
            while left <= right and s[left] == c:
                left += 1
            # 右边往前找
            while left <= right and s[right] == c:
                right -= 1
        return right - left + 1

s = Solution()
ans = s.minimumLength('aaaa')
print(ans)