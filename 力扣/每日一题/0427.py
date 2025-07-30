# 3392. 统计符合条件长度为 3 的子数组数目
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        res = 0
        l = 0
        r = 2
        while r < len(nums):
            if 2 *(nums[l] + nums[r]) ==  nums[l + 1]:
                res += 1
            l, r = l + 1, r + 1
        return res
