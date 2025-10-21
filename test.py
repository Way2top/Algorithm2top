n = int(input())
s = [0] * n
k = [0] * n
string = []
for i in range(n):
    s[i], k[i] = map(int, input().split())
    string.append(input())

# 为了让 Teto 无法更改内容，我们需要
# 1. 考虑数字 1，对于1来说，它受保护 or 