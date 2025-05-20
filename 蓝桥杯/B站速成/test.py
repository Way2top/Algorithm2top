from functools import *


@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 测试代码
n = 80
print(fibonacci(n))
