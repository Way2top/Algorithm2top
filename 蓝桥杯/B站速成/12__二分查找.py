from bisect import bisect

# 1. 不递减的数组，找到第一个严格大于某元素的下标
# a = [1, 9, 9, 9, 200, 500]
# res = bisect(a, 9)
# print(res) # output：4

# 2. 不递减的数组，找到第一个大于等于某元素的下标
# a = [1, 9, 9, 9, 200, 500]
# res = bisect(a, 9 - 1)
# print(res)  # output：1

# 3. 不递减的数组，找到恰好小于等于某元素的下标
a = [1, 9, 9, 9, 200, 500]
res = bisect(a, 9) - 1  # 小于等于某元素，就是大于某元素的下标减1
print(res)  # output：1
