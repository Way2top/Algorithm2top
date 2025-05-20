# T586706 我是黄色恐龙大将军

res = set()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a:
    for j in b:
        res.add(i * j)

print(sum(res))
