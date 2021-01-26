# 위에서 아래로
# N을 입력받는다
n = int(input())

# N개의 정수를 입력받아 리스트에 저장한다
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

print(array)