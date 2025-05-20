def solution(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


n = int(input())
count = solution(n)
res = 0
for i in count:
    if n % i == 0:
        res += 1

print(res)