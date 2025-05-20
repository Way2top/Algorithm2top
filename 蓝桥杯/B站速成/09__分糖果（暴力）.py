# 蓝桥云课

# 输入
n = int(input())
nums = list(map(int, input().split()))

res = 0  # 老师要补发的糖果数量

while True:
    count = 0
    # 如果每个人的糖果数相同，退出循环
    for i in range(n):
        if nums[i] == sum(nums) / n:
            count += 1
    if count == n:
        break

    # 如果糖果数量不一致
    temp = []
    for i in range(n):
        temp.append(nums[i] // 2)
    # 每个人给一半左手边孩子
    nums[n - 1] = temp[n - 1] + temp[0]
    for i in range(n - 1):
        nums[i] = temp[i] + temp[i + 1]

    # 发完之后检查是否有奇数项的孩子
    for i in range(n):
        if nums[i] % 2 == 1:
            nums[i] += 1
            res += 1

print(res)
