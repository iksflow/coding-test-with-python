# 피보나치 수열 계산함수(재귀적 풀이 - 탑다운) 다이나믹 프로그래밍과 메모이제이션 기법을 적용
d = [0] * 100
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    else:
        d[n] = fibo(n - 1) + fibo(n - 2)
        return d[n]

print(fibo(99))
