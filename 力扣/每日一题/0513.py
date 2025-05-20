# Leetcode:3335
class Solution:
  def lengthAfterTransformations(self, s: str, t: int) -> int:
    MOD = 10**9 + 7
    dp = [1] * 26

    for i in range(t):
        new_dp = [0] * 26
        # z
        new_dp[25] = (dp[0] + dp[1]) % MOD
        # a - y
        for i in range(25):
            new_dp[i] = dp[i + 1]
        
        dp = new_dp
    
    res = 0
    for ch in s:
        index = ord(ch) - ord('a')
        res = (res + dp[index]) % MOD
    
    return res