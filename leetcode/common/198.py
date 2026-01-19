class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp[i] 代表偷到第 i 家的时候可以窃取到的最高金额
        # 题目说相邻不可偷，因此 dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) # 两家只能选一家
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]
        