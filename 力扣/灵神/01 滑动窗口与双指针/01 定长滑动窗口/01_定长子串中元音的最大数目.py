# # Leetcode：1456
# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vowel = ('a', 'e', 'i', 'o', 'u')
#         count = 0  # 记录包含元音字母的个数
#         res = 0
#
#         n = len(s)
#         # 先把第一组的算出来
#         for i in range(k):
#             if s[i] in vowel:
#                 count += 1
#                 res = count
#
#         for i in range(1, n - k + 1):
#             if s[i - 1] in vowel:
#                 count -= 1
#             if s[i - 1 + k] in vowel:
#                 count += 1
#
#             res = max(res, count)
#         return res
#
#
# solution = Solution()
# ans = solution.maxVowels('abciiidef', 3)
# print(ans)

# Leetcode：1456
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ('a', 'e', 'i', 'o', 'u')
        count = 0
        res = 0

        for i, c in enumerate(s):
            if c in vowel:
                count += 1
            if i < k - 1:
                continue

            res = max(count, res)

            if s[i - k + 1] in vowel:
                count -= 1
        return res


solution = Solution()
ans = solution.maxVowels('abciiidef', 3)
print(ans)