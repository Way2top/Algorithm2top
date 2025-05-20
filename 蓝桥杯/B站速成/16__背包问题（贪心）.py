# 洛谷：P2240 【深基12.例1】部分背包问题

import sys

input = lambda: sys.stdin.readline().strip()

n, T = map(int, input().split())

treasure = [[0, 0]] * n
for i in range(n):
    treasure[i] = list(map(int, input().split()))

# 根据单位价格从高到低排序，先把高价格拿满
treasure.sort(key=lambda x: (x[1] / x[0]), reverse=True)

res = 0
bag = 0  # 记录背包的重量
# for i, t in enumerate(treasure):
#     print(t[0], t[1])


for trea in treasure:
    if (T - bag) >= trea[0]:
        res += trea[1]
        bag += trea[0]
    else:
        res += (T - bag) * (trea[1] / trea[0])
        bag += T - bag
        break

print(f'{res:.2f}')
