class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # i, j, k, 其中，要求任意两数之和大于第三个数
        nums.sort(reverse=True) # 倒序排序
        # 排序之后，如果设定 i < j < k，那么只需要满足 nums[j] + nums[k] > nums[i] 即可
        ans = 0
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s > nums[i]:
                    ans += k - j
                    j += 1
                else:
                    k -= 1
        return ans
        