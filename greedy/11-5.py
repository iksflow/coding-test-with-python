# 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 두 사람이 고르는 볼링공 무게는 달라야 한다.
# 볼링공의 무게는 10까지 있으므로 무게별 개수를 저장할 리스트를 만든다.

balls = [0] * 11

for weight in data:
    balls[weight] += 1

result = 0

for i in range(1, m + 1):
    n -= balls[i]
    result += balls[i] * n
    print('n = ', n)

print(result)
