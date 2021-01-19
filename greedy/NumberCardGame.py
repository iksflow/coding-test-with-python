n, m = map(int, input().split())

result = 0
# 해결법 1. min()이용
# # 한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)

# 해결법 2. 2중 반복문
for i in range(n):
    data = list(map(int, input().split()))
    minValue = 10001
    for j in range(len(data)):
        minValue = min(minValue, data[j])

    result = max(result, minValue)

print(result)