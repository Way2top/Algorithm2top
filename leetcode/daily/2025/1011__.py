class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        # 要求最大值，等价于求在(power[i] - 2, power[i] + 2) 之间的最小值
        # dp[i] = dp[i - 1] + power[i]
        # dp[i] 的含义是走到第 i 个咒语的时候可以造成伤害的最大值
        
        