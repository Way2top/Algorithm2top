# 洛谷：P2367 语文成绩
import sys

input = lambda: sys.stdin.readline().strip()

# 读取学生数量 n 和操作次数 p
n, p = map(int, input().split())
# 读取每个学生的初始成绩
a = list(map(int, input().split()))

# 初始化差分数组
diff = [0] * n
diff[0] = a[0]
for i in range(1, n):
    diff[i] = a[i] - a[i - 1]

# 直接处理每个操作，不使用 op 数组存储
for _ in range(p):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    diff[x] += z
    if y + 1 < n:
        diff[y + 1] -= z

# 从差分数组还原出更新后的成绩数组
for i in range(1, n):
    diff[i] += diff[i - 1]

# 找出更新后成绩的最小值
print(min(diff))