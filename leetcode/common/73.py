# class Solution:
#     def setZeroes(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = []
#         col = []
#         m = len(matrix)
#         n = len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row.append(i)
#                     col.append(j)
        
#         # 现在 row 和 col 中就是所有行和列需要变成 0 的元素了
#         for r in row:
#             for i in range(n):
#                 matrix[r][i] = 0
#         for i in range(m):
#             for c in col:
#                 matrix[i][c] = 0

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # 对于第一行和第一列的 0，我们用额外一个变量记录
        # 因为如果不用额外的记录的话，会导致状态丢失
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n)) # 记录第一行中是否存在 0
        first_col_zero = any(matrix[i][0] == 0 for i in range(m)) # 记录第一列中是否存在 0

        # 先处理 (1, m) 和 (1, n)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # 在该行的第一列做标记
                    matrix[0][j] = 0 # 在该列的第一行做标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 然后单独处理第一行和第一列
        if first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


s = Solution()
res = s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(res)