class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        path = [-1] * n # path[i] 代表第 i 行第 path[i] 列为皇后

        cols = set()
        line_1 = set() # 正对角线
        line_2 = set() # 副对角线

        # 将 path 处理，构造出符合要求的答案形式
        def build_ans(p: list, n: int):
            chess = []
            for i in range(n): # i 代表第 i 行
                temp = ['.'] * n
                temp[path[i]] = 'Q'
                chess.append(''.join(temp))
            return chess

        def dfs(row: int): # 表示处理第 row 行
            if row == n:
                ans.append(build_ans(path, n))
                return

            for col in range(n):
                if col in cols or (row - col) in line_1 or (row + col) in line_2:
                    continue
                cols.add(col)
                line_1.add(row-col)
                line_2.add(row+col)
                path[row] = col
                dfs(row+1)
                path[row] = -1
                cols.remove(col)
                line_1.remove(row-col)
                line_2.remove(row+col)
        dfs(0)
        return ans
                