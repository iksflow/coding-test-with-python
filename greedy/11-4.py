# 만들 수 없는 금액

n = int(input())
data = list(map(int, input().split()))

# 작은 동전부터 처리하도록 정렬
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)


