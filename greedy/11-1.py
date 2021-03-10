# 모험가 길드

n = int(input())
array = list(map(int, input().split()))

print('n=', n, ', array=', array)

# 풀이 아이디어 : 가장 공포도가 작은 모험가들부터 그룹을 지어 보낸다.

# 오름차순 정
array.sort()

print('array after=', array)

# 그룹의 수
count = 0

# 공포도
fear = -1;

for i in n:
    if fear == -1:
        fear = array[i]
    elif fear == 0:
        fear = array[i]
        count = count + 1

    fear = fear - 1

print("maked group =", count)


