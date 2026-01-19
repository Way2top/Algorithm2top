class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            temp = [0] * (i+1)
            # 第一个元素与最后一个元素
            temp[0], temp[-1] = ans[i - 1][0], ans[i - 1][-1]
            # 剩余元素
            for k in range(1, i):
                temp[k] = ans[i - 1][k - 1] + ans[i - 1][k]
            ans.append(temp)
        return ans
            