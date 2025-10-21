class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        res = []
        while left <= right and top <= bottom:
            # Step1: 在 top 从 left 到 right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1  # top 走完了要向下移动一层

            # Step2：在 right 从 top 到 bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # right 走完了要向左移动一层

            # Step3：在 bottom 从 right 到 left
            if top <= bottom:  # 因为前面 top += 1 了
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
            bottom -= 1  # bottom 走完了要向上移动一层

            # Step4：在 left 从 bottom 到 top
            if left <= right:  # 因为前面 right -= 1 了
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
            left += 1
        return res
