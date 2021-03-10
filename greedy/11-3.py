# 문자열 뒤집기

s = input()

n = int(s[0])
result = [0] * 2
result[n] = 1
print('result =', result)
for i in range(1, len(s)):
    if int(s[i]) == n:
        continue
    else:
        result[n] += 1
        n = int(s[i])

print('result =', result)
print('answer =', min (result[0], result[1]))

