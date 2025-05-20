# T588725 化食欲为动力

# # 先把最大的 c 找出来，因为 a * b无论多大，最终和 c 做模运算，值的大小都是取决于 c 的
# def solution(a, b, c):
#     max_mod = max(c)
#     and_set = set()  # a * b 的集合
#     for i in a:
#         for j in b:
#             and_set.add(i * j)
#
#     max_res = 0
#     for num in and_set:
#         # 当 c = (a * b) // 2 + 1的时候，题目目标值最大为 c - 1(a * b 为奇数) 或者 c - 2(a * b为偶数)
#         if num == (max_mod - 1) * 2:
#             print(num % max_mod)
#             return
#         else:
#             max_res = max(max_res, num % max_mod)
#
#     print(max_res)
#
#
# n, m, k = list(map(int, input().split()))
#
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
#
# solution(a, b, c)


# 暴力拿40分得了
n, m, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

max_num = 0
for i in a:
    for j in b:
        for t in c:
            max_num = max((i * j) % t, max_num)

print(max_num)
