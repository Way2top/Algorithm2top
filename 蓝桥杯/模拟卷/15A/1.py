# n2表示2x2方块数量，n1表示1x1方块数量
n2 = 7385137888721
n1 = 10470245

max_length = 0
cur_length = 1

while True:
    n2_max = cur_length * cur_length // 4
    n1_max = cur_length * cur_length % 4

    if n2_max < n2 and n1_max < n1:
        max_length = cur_length
    else:
        break

    cur_length += 1

print(max_length)