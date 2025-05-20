# T589116

year1 = 2025  # 45的平方
year2 = 2116  # 46的平方

total = 0
for year in range(2026, 2116):
    if year % 100 != 0 and year % 4 == 0:
        total += 366
    elif year % 100 == 0 and year % 400 == 0:
        total += 366
    else:
        total += 365

# 2025剩下的天数
total += 275 + 2
print(total)
