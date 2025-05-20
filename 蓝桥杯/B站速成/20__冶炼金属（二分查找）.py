# 洛谷：P9240 [蓝桥杯 2023 省 B] 冶炼金属
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())


# def check_min(v):

