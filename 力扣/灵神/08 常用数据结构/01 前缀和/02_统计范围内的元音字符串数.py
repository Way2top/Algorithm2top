# Leetcode:2559
class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        n = len(words)
        vowel = ('a', 'e', 'i', 'o', 'u')
        # 将 words 中以元音开头和结尾的都替换成 1，其余为 0
        arr = []
        for ch in words:
            if ch[0] in vowel and ch[-1] in vowel:
                arr.append(1)
            else:
                arr.append(0)
        # 构建 arr 的前缀和数组
        prefix = [0] * (n + 1)
        for i, x in enumerate(arr):
            prefix[i + 1] = prefix[i] + x
        
        # 遍历 queries 数组，统计结果
        ans = []
        for left, right in queries:
            ans.append(prefix[right + 1] - prefix[left])
        return ans