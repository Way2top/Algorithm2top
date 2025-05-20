dic = {
    0: '1111110',
    1: '0110000',
    2: '1101101',
    3: '1111001',
    4: '0110011',
    5: '1011011',
    6: '1011111',
    7: '1110000',
    8: '1111111',
    9: '1111011'
}

codes = ['0000011',
         '1001011',
         '0000001',
         '0100001',
         '0101011',
         '0110110',
         '1111111',
         '0010110',
         '0101001',
         '0010110',
         '1011100',
         '0100110',
         '1010000',
         '0010011',
         '0001111',
         '0101101',
         '0110101',
         '1101010']

possible = {}
for code in codes:
    # 每一轮循环都和dic中的10个数字比较，如果
    mark = 0
    for dic_code in dic.items():
        count = 0
        for i in range(7):
            # 数字为0的时候无所谓，但是数字为1的时候，dic_code中对应的数字也必须为1才能确定可以是这个数，否则不行（也就是code[i] 为1但是dic_code[i]为0的情况）
            if code[i] == '1' and dic_code[1][i] == '0':
                count = 0
                break
            else:
                count += 1
        if count == 7:
            mark += 1
    possible[code] = mark

res = 1
for i in possible.values():
    res *= i

print(res)

# dic = {
#     0: '1111110',
#     1: '0110000',
#     2: '1101101',
#     3: '1111001',
#     4: '0110011',
#     5: '1011011',
#     6: '1011111',
#     7: '1110000',
#     8: '1111111',
#     9: '1111011'
# }
#
# codes = ['0000011',
#          '1001011',
#          '0000001',
#          '0100001',
#          '0101011',
#          '0110110',
#          '1111111',
#          '0010110',
#          '0101001',
#          '0010110',
#          '1011100',
#          '0100110',
#          '1010000',
#          '0010011',
#          '0001111',
#          '0101101',
#          '0110101',
#          '1101010']
#
# total_possible = 1
# for code in codes:
#     possible_count = 0
#     for num, dic_code in dic.items():
#         valid = True
#         for i in range(7):
#             if code[i] == '1' and dic_code[i] == '0':
#                 valid = False
#                 break
#         if valid:
#             possible_count += 1
#     total_possible *= possible_count
#
# print(total_possible)
