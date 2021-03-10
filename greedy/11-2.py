# 곱하기 혹은 더하기

# 숫자로 이루어진 문자열
s = input()

# 숫자들 끼리 덧셈 혹은 곱셈을 해서 가장 큰 수를 만들어라.
# 접근 아이디어
# 수가 1 이하라면 덧셈으로 처리한다. 그 이유는 곱셈을 해봤자 값이 그대로이거나 0이 되어버리기 때문
# 수가 2 이상이라면 곱셈으로 처리한다.
result = int(s[0])
for i in range(1, len(s)):
    n = int(s[i])
    if result == 0 or n < 2:
        result += n
    else:
        result *= n

print('maximum value =', result)
