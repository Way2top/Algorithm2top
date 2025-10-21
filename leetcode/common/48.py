class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for k in range(i):
                matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]
        
        for row in matrix:
            row.reverse()
