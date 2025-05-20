def euler_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            
            if i % p == 0:
                break
    return primes

print(euler_sieve(20))