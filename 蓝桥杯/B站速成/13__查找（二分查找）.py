# 洛谷 P2249 【深基13.例1】查找
from bisect import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
nums = list(map(int, input().split()))

ans = []
for q in nums:
    res = bisect(a, q - 1)
    if res == n or a[res] != q:
        ans.append(-1)
    else:
        ans.append(res + 1)

for i in ans:
    print(i, end=' ')
