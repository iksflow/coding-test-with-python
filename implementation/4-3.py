# 왕실의 나이트
input_str = input()
row = int(input_str[1])
column = int(ord(input_str[0])) - int(ord('a')) + 1
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
result = 0
for i in range(len(steps)):
    step = steps[i]
    if row + step[0] < 1 or column + step[1] < 1 or row + step[0] > 8 or column + step[1] > 8:
        continue
    result += 1
print(result)