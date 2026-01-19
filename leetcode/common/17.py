class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combo = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'] # combo[i] 代表按下数字 i 对应的字母映射
        n = len(digits)
        if n == 0:
            return []
        
        ans = []
        path = [''] * n
        def dfs(i: int):
            if i == n:
                ans.append(''.join(path))
                return
            for c in combo[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
        dfs(0)
        return ans

s = Solution()
res = s.letterCombinations('23')
print(res)
        