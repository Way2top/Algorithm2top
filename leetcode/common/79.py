class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int, idx: int) -> bool:
            # 1. 当前字符不匹配，直接失败
            if board[x][y] != word[idx]:
                return False

            # 2. 已经匹配到最后一个字符
            if idx == len(word) - 1:
                return True

            visited[x][y] = True

            # 3. 向四个方向扩散
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if dfs(nx, ny, idx + 1):
                        return True

            # 4. 回溯
            visited[x][y] = False
            return False

        # 5. 枚举起点
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
