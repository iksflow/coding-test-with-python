# 개미 전사

n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

# D[i] i + 1번째 창고를 털었을 때 최대 값
# D[0] = 1번째 창고를 털었을 때 최대값
# 2번째 창고를 털었을 때 최대값
# D[1] = max(D[0], D[1])
# 3번째 창고를 털었을 때 최대값
# D[2] = max(D[2] + D[0], D[1])
# ...
# D[i] = max(D[i] + D[i - 2], D[i - 1])

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
