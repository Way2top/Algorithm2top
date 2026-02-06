class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s) 

        def dfs(start: int): # start 表示分割指针
            if start == n:
                ans.append(path[:])
                return
            for i in range(start, n):
                sub_str = s[start:i]
                if sub_str == sub_str[::-1]:
                    path.append(sub_str)
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return ans