class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            temp = m - self.bisect_left(potions, success / spells[i]) 
            pairs[i] = temp
        return pairs

    # 返回第一个等于 target 的下标
    def bisect_left(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo