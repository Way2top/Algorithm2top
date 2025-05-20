# T588424 扶苏出勤日记

t = int(input())
n = []
a = []
b = []
for _ in range(3):
    n.append(int(input()))
    temp_a = list(map(int, input().split()))
    a.append(temp_a)
    temp_b = list(map(int, input().split()))
    b.append(temp_b)


def solution(t, n, a, b):
    # 处理每组数据
    for i in range(t):
        day = n[i]  # 日期
        cost = a[i]  # 成本
        income = b[i]  # 收入
        times = 0  # 每日游玩次数
        for j in range(day):
            times = income[j] * cost[j]
            
