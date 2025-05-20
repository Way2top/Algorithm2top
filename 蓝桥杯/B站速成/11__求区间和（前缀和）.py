# 洛谷 P8218 【深进1.例1】求区间和

# 输入
n = int(input())
a = list(map(int, input().split()))
m = int(input())

section = [[0, 0]] * m
for i in range(m):
    section[i] = list(map(int, input().split()))
    # 此题下标从1开始的，处理成习惯的从0开始
    section[i][0] -= 1
    section[i][1] -= 1

# 构建前缀和数组
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

for i in range(m):
    l, r = section[i]  # 左区间和右区间
    print(p[r + 1] - p[l])
