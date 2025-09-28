import math

dict = {1:2, 3:4}
print(type(dict.values()))

stack = [1, 2, 3]
stack.pop()
print(len(stack))

def getDigit(n : int) -> list[int]:
    res = []
    while n > 0:
        res.append(n % 10)
        n //= 10
    res.reverse()
    return res

res = getDigit(123)
print(res)

a = math.inf
print(a)