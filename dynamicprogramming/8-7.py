# 바닥 공사
# 점화식
# 1번째 : D[0] = 1개 / 2 * 1 타일만 가능
# 2번째 : D[1] = 3개 / 1 * 2 2개, 2 * 1 2개, 2 * 2 1개 총 3가지 가능
# 3번째 : D[2] = D[1] + 2 * 1 그리고 D[0] + 3가지
# ...
# n번째 : D[n] = D[n-1] + D[n-2] * 2

n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])
