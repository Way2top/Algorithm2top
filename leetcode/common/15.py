# 双指针
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            # 去除重复答案
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else: # total == 0
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 # 去除重复答案
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res
