n = int(input())
nums = list(map(int, input().split()))

count = 0

for i in nums:
    if i == 1 or i == 2:
        count += 1

    # 奇数一定是诗意数字
    elif i % 2 == 1:
        continue

    # 偶数
    else:
        if i % 4 == 0:
            count += 1
        else:
            continue

print(count)

