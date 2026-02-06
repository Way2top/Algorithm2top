class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(start: int, x: int, y: int) -> bool:
            if board[x][y] != word[start]:
                return False
            if start == len(word) - 1: # board[x][y] == word[start] and start == len(word) - 1
                return True
            if visited[x][y]: # 如果当前元素访问过
                return False  
            
            visited[x][y] = True
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= i < m and 0 <= j < n and not visited[i][j] and board[i][j] == word[start+1]:
                    if dfs(start+1, i, j):
                        return True
            visited[x][y] = False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False
