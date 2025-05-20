# 蓝桥云课：最大数字
import sys

input = lambda: sys.stdin.readline().strip()

n, a, b = map(int, input().split())


# 拿出一个数的每个位数
def get_digit(x):
    number_list = []
    while x > 0:
        number_list.append(x % 10)
        x = x // 10
    return number_list[::-1]


# 对同一位数字，一定只会执行 + 操作或者 - 操作，不会混着用
digit = get_digit(n)
# 从高位开始遍历
for i in range(len(digit)):
    if digit[i] <= b:
        digit[i] = 9
        b -= digit[i]
    elif digit[i] + a >= 10:
        digit[i] = 9
        a -= digit[i]
    else:
        digit[i] += a
        a = 0

res = 0
for i, d in enumerate(digit[::-1]):
    res += d * pow(10, i)
print(res)
