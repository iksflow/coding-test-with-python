# 부품탐색 계수정렬 성질 이용한 풀이. map성질

# 보유 수량
n = int(input())

# 저장할 공간 생성. 고객이 요구할 가지수는 100,000이므로 리스트의 크기를 100,001로 초기화
array = [0] * 100001

# 내가 보유한 부품 가지수 체크
for i in input().split():
    array[int(i)] = 1

# 고객의 수량
m = int(input())

# 고객이 원하는 항목 수 확인하며 출력
for i in input().split():
    if array[int(i)] == 1:
        print("yes", end = " ")
    else:
        print("no", end=" ")

