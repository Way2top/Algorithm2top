# Leetcode：1652
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        # 延长code，方便处理
        code += code
        res = []

        if k == 0:
            return [0] * n

        if k > 0:
            l, r = 1, k
        else:
            l, r = n + k, n - 1

        # 初始化第一个元素
        w = sum(code[l:r + 1])
        for i in range(n):
            res.append(w)
            w -= code[l]
            w += code[r + 1]
            l, r = l + 1, r + 1
        return res
