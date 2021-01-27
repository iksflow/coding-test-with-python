# 피보나치 수열 계산함수(반복적 풀이 - 바텀업)


def fibo(n):
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    count = 1
    while count <= n:
        if d[count] == 0:
            d[count] = d[count - 1] + d[count - 2]
        count += 1
    return d[n]


print(fibo(6))