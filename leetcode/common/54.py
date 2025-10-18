class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # Step1: 在 top 从左往右遍历
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Step2: 在 right 从上往下遍历
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Step3: 在 bottom 从右往左遍历
            if top <= bottom: # 这里要判断，因为前面
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # Step4: 在 left 从下往上遍历
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
