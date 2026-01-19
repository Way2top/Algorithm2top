class Solution:
    def upper_bound(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        last_val = [] # 每一行最后一个元素组成的列表，递增且无重复
        for i in range(n):
            last_val.append(matrix[i][m - 1])
        
        # 判断元素在哪一行
        n_idx = self.upper_bound(last_val, target)

        # target 大于 last_val[-1]，也即 target 大于整个二维矩阵，那么直接返回 False
        if n_idx == n:
            return False
        
        # 否则就找到了 target 所在的行索引：n_idx
        # 接下来就在该行找是否存在 target
        m_idx = self.upper_bound(matrix[n_idx], target)

        # 没找到的情况
        if m_idx == m or matrix[n_idx][m_idx] != target:
            return False

        # 找打了
        return True
        