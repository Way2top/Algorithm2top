# P10387
# 贪心 + 排序

n, s = map(int, input().split())

nums = [[0, 0]] * n
p = [0] * n
c = [0] * n

for i in range(n):
    nums[i] = list(map(int, input().split()))

# 根据训练次数排序
nums.sort(key=lambda x: x[1])

for i in range(n):
    p[i], c[i] = nums[i][0], nums[i][1]

res = 0  # 训练总花费
count = 0  # 团购训练次数
total = sum(p)  # 训练一遍所有士兵的花费

# 每次循环训练完一个士兵，当有士兵结束训练完成后total才会更新
for i in range(n):
    if total >= s:
        res += (c[i] - count) * s
        count = c[i]

    else:
        res += (c[i] - count) * p[i]

    total -= p[i]

print(res)
