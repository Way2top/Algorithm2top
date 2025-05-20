def solution(n):
    primes = []
    is_primes = [True] * (n + 1)
    is_primes[1] = is_primes[0] = False
    
    for i in range(2, n + 1):
        if is_primes[i]:
            for j in range(i * i, n + 1, i):
                is_primes[j] = False

    for i in range(n + 1):
        if is_primes[i]:
            primes.append(i)
    return primes


res = solution(10000)
print(res)
