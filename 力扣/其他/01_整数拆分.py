# Leetcode:343
class Solution:
    def integerBreak(self, n: int) -> int:
        # create a dp array, where dp[i] represents the maximum product of number i
        dp = [1] * 59
        dp[2] = 2
        
        for i in range(59):
            pass
        
    def get_prime(num):
        primes = []
        is_primes = [True] * (num + 1)

        for i in range(2, num + 1):
            if is_primes[i]:
                primes.append(i)
            
            for p in primes:
                if i * p > num:
                    break
                
