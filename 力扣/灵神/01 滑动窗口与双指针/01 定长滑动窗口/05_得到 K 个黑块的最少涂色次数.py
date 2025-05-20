# Leetcode：2379
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count = 0
        res = 0

        # 初始化第一个窗口
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        res = count

        # 向后滑动，动态改变count次数
        for i in range(1, n - k + 1):
            if blocks[i-1] == 'W':
                count -= 1

            if blocks[i-1+k] == 'W':
                count += 1

            res = min(res, count)

        return res
