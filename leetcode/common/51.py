class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        # path 可以用一个一维数组就表示整个棋盘的状态，这是因为N皇后的规则决定了一行有且只有一个皇后，不可能出现一行多个皇后
        path = [-1] * n # path[row] 表示第 row 行第 path[row] 列为皇后
        cols = set() # 用于记录当前列包含的皇后
        diag1 = set() # 用于记录主对角线（row - col）
        diag2 = set() # 用于记录副对角线（row + col）
        
        def build_ans(position: list, n: int):
            # 辅助函数，将 path 构造为符合题目要求的答案
            answer = []
            for i in range(n):
                temp = ['.' for _ in range(n)]
                temp[position[i]] = 'Q'
                answer.append(''.join(temp))
            return answer
        
        def dfs(row: int): # row 表示从 row 行开始找皇后
            if row == n:
                ans.append(build_ans(path, n))
                return
            
            for col in range(n): # 遍历第 row 行的每一列
                # 当前元素的坐标为(row, col)
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # 做选择
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                path[row] = col
                # 递归
                dfs(row+1)
                # 撤销
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        dfs(0)
        return ans

                