# B2129
# 递归

a, b, c = list(map(int, input().split()))

result = max(a, b, c)/(max(a + b, b, c) * max(a, b, b + c))

print(f'{result:.3f}')
