class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int, start: int) -> bool:
            if board[x][y] != word[start]:
                return False
            if start == len(word) - 1: # 如果 board[x][y] == word[start] 且 start 为 word 的最后一个元素的下标
                return True
            # 开始对当前元素 board[x][y] 进行操作
            visited[x][y] = True # 标记为已使用
            for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<= dx < m and 0 <= dy < n and not visited[dx][dy]:
                    if dfs(dx, dy, start+1):
                        return True
            visited[x][y] = False
            return False
                
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
