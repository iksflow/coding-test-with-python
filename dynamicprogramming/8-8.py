# 효율적인 화폐구성

# 정수 N, M을 입력받는다
n, m = map(int, input().split())

# N개의 화폐단위 정보를 받을 자료구조
array = []

# N개의 화폐단위를 입력받는다.
for i in range(n):
    array.append(int(input()))

# 한번 계산한 결과를 저장하기 위해 DP테이블을 정의한다
d = [10001] * (m + 1)
d[0] = 0
for x in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)


# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])