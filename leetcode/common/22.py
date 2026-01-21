class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        path = []
        
        def dfs(left: int, right: int):
            if left == n and right == n:
                ans.append(''.join(path))
                return
            
            # 可以添加 (
            if left < n:
                path.append('(')
                dfs(left+1, right)
                path.pop()
            
            # 可以添加 )
            if left > right:
                path.append(')')
                dfs(left, right+1)
                path.pop()
        dfs(0, 0)
        return ans