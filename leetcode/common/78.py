class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = []
        
        def dfs(l: int, idx: int): # l 表示子集长度，idx 表示开始的下标
            if len(path) == l:
                ans.append(path.copy()) 
                return
            
            for i in range(idx, n):
                path.append(nums[i])
                dfs(l, i+1)
                path.pop()
        for length in range(n):
            dfs(length, 0)
        ans.append([])
        return ans
        
            