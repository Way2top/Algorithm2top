# 洛谷：P1102 A-B 数对
def solve():
    # 读取输入
    N, C = map(int, input().split())
    nums = list(map(int, input().split()))

    # 用字典统计每个数字出现的次数
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # 计算满足条件的数对个数
    result = 0
    for b in nums:
        a = b + C  # 需要找的 A = B + C
        if a in freq:
            # 对于每个 b，找到所有可能的 a
            # 如果 a 和 b 是同一个数，需要减去自己与自己配对的情况
            if a == b:
                result += freq[a] * (freq[a] - 1)
            else:
                result += freq[a] * freq[b]

    # 因为每对都被计算了两次（从a和b两个方向），所以结果除以2
    return result // 2


# 输出结果
print(solve())
