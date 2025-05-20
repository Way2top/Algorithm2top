import sys

input = lambda: sys.stdin.readline().strip()

# 单行多个数
# a, b, c = map(int, input().split())

# 多行多个整数
n = int(input())
lst = [int(input()) for _ in range(n)]
print(lst)
