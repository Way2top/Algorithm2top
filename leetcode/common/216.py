class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # 从 1~9 中选出 k 个数，要求这 k 个数之和为 n，找出所有的有效组合
        ans = []
        # 对于每一次 dfs，我需要知道距离 n 还剩下多少，还需要知道当前使用到了第几个数
        path = []
        visited = [False for _ in range(10)]

        def dfs(idx: int, remain: int):
            if idx == k - 1 and remain == 0:
                ans.append(path.copy())
                return
            
            if remain < 0:
                return
            
            # remain > 0
            for num in range(1, 10):
                if visited[num] == False:
                    path.append(num)
                    dfs(idx + 1, remain - num)
                    visited[num] = True

        dfs(0, n)
        return ans
                
            
            
        