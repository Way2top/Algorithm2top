class Solution:
    def isVowel(self, s: str) -> bool:
        vowel = 'aeiou'
        if s[0] in vowel and s[-1] in vowel:
            return True
        return False
    
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        n = len(words)
        prefix = [0] * (n + 1) # prefix[i] 表示前 i 个元素中满足要求的字符数
        # 计算 prefix 数组
        for i in range(n):
            if self.isVowel(words[i]):
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        res = []
        for left, right in queries:
            res.append(prefix[right + 1] - prefix[left])
        return res