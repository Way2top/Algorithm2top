class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 重要的是将字符串全部转化为小写并移除所有非字母数字字符
        # 移除非字母数字字符
        processed_s = ''.join(c for c in s if c.isalnum())
        # 小写
        processed_s = processed_s.lower()

        # 接下来就是很简单的双指针判断了
        left, right = 0, len(processed_s) - 1
        while left < right:
            if processed_s[left] == processed_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
        