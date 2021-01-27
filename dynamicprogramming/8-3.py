# 피보나치 함수를 처리할 때 호출되는 재귀함수 순서 확인하기
d = [0] * 100
def fibo(n):
    print("fibo(" + str(n) + ")", end = " ")
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    else:
        d[n] = fibo(n - 1) + fibo(n - 2)
        return d[n]

print(fibo(6))
