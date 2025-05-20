# 召唤数学精灵
n = 2024041331404202

a = 0
count = 0

for i in range(n):
    a += i
    if a % 100 == 0:
        count += 1
        a = a % 100

print(count)
