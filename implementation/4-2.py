n = int(input())

# 00시 00분 00초 ~ 00시 59분 59초(n = 0)
# 3분, 13분, 23분, 30~39분, 43분, 53분 > 1+ 1+ 1 + 10 + 1 + 1 = 15 * 60 = 900
# 3초, 13초, 23초, 30~39초, 43초, 53초 > 0 ~ 60 - 15 = 45 * 15 = 675
# n = 0 : 15 , n = 1 : 30, n = 3 60 * 60 = 3600
# 3n시 = 3600, 3분 = 60
result = 0
for i in range(n+1):
    if (i % 3 == 0) and 0 < i:
        result += 3600
    else:
        result += 1575

print(result)