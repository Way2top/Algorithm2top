class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = []
        used = [False] * n

        def dfs():
            if len(path) == n:
                ans.append(path.copy())
                return
            
            for i, x in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(x)
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return ans
        