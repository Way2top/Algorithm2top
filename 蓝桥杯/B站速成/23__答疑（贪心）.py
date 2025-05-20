# 洛谷：P8732 贪心
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = []
a = []
e = []

for i in range(n):
    x, y, z = map(int, input().split())
    s.append(x)
    a.append(y)
    e.append(z)

print(s)
print(a)
print(e)

res = 0
