class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(start: int):
            if len(path) == k:
                ans.append(path.copy())
                return
            # 剪枝：如果 path 的现有元素个数加上 (start, n + 1) 的总数都不够 k，那就不需要继续组合了
            if n - start + 1 + len(path) < k:
                return
            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1)
                path.pop()
        dfs(1)
        return ans
