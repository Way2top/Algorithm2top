class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        n = len(candidates)
        
        def dfs(idx: int, remain: int): # idx 表示从下标 idx 开始遍历 candidates，remain 表示距离 target 还剩 remain
            if remain == 0:
                ans.append(path.copy())
                return
            if remain < 0:
                return
            for i in range(idx, n):
                path.append(candidates[i])
                dfs(i, remain - candidates[i])
                path.pop()
                
        dfs(0, target)
        return ans
                
        