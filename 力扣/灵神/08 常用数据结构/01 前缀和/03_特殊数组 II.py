class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        prefix = [0] * n
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        res = []
        for left, right in queries:
            if prefix[right] - prefix[left] == 0:
                res.append(True)
            else:
                res.append(False)
        return res
