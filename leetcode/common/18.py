class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
        return ans
                        
        