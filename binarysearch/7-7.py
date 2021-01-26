# 부품 찾기 집합 자료구조를 이용한 풀이
n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
for i in input().split():
    if int(i) in n_set:
        print("yes", end=" ")
    else:
        print("no", end=" ")
