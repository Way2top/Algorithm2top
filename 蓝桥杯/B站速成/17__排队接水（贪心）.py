# 洛谷：P1223 排队接水

import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
t = list(map(int, input().split()))

res = 0  # 平均等待时间

dic = {}
for i in range(n):
    dic[i + 1] = t[i]

l = sorted(dic.items(), key=lambda x: x[1])

wait = []
cur = 0
for i in range(n):
    print(l[i][0], end=' ')
    wait.append(cur)
    cur += l[i][1]

aver = sum(wait) / n
print()
print(f'{aver:.2f}')
