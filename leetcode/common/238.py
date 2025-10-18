class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        # 先求前缀积
        for i in range(1, n):
            # ans[i] 存储的是 nums[0] * nums[1] * ... * nums[i-1] 的结果。
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # 此时 ans[i] 代表在 i 之前的所有元素的乘积
        # 按照题目要求，我们还需要计算出在 i 之后的所有元素的乘积，然后与 ans[i] 相乘
        # 我们可以把求出后缀积和与前缀积相乘得到答案的这两步合为一步
        right = 1
        for i in range(n - 1, -1, -1): # 从最后一个元素往前遍历
            ans[i] *= right
            right *= nums[i]
        return ans