# P1010

def solution(n):
    # 递归结束条件
    if n == 0:
        return "0"
    if n == 2:
        return "2"
    if n == 1:
        return "2(0)"
    # 将 n 转换为二进制
    bn = bin(n)[2:]
    parts = []
    for i, bit in enumerate(reversed(bn)):
        if bit == '1':
            if i == 1:
                parts.append("2")
            else:
                parts.append(f"2({solution(i)})")
    return "+".join(parts)


print(solution(137))

