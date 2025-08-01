s = 'abcd'
t = 'bcdf'
res = []

for i in range(len(s)):
    res.append(abs(ord(s[i]) - ord(t[i])))

print(res)