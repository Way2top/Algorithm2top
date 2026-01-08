import math

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = 0
        minDiff = math.inf
        n = len(nums)
        for i in range(n - 2):
            # 优化 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # 优化 2
            s = nums[i] + nums[i + 1] + nums[i + 2]
            if s > target:
                if s - target < minDiff:
                    ans = s
                break
            
            # 优化 3
            s = nums[i] + nums[-1] + nums[-2]
            if s < target:
                if target - s < minDiff:
                    minDiff = target - s
                    ans = s
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    ans = s
                    break
                elif s > target:
                    if s - target < minDiff:
                        minDiff = s - target
                        ans = s
                    k -= 1
                else: # s < target
                    if target - s < minDiff:
                        minDiff = target - s
                        ans = s
                    j += 1
        return ans 