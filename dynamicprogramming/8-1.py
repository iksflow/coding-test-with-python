# 피보나치 수열의 n번째 값을 구하는 함수 구현

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# 1 1 2 3 으로 4번째 값인 3이 출력된다.
print(fibo(4))


