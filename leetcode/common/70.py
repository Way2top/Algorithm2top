class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)# dp[i] 代表爬 i 级台阶的方法有多少种
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]