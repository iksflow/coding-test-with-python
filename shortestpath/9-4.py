# 미래 도시
# 접근 방법 : 1번회사 - K번회사 - X번회사의 순으로 방문할 계획.
# 즉 1 - K 의 최단경로 + K - X 의 최단경로를 더해야함.

# 회사의 개수 N, 경로의 개수 M을 입력 받기
n, m = map(int, input().split())

INF = int(1e9)
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 거리 0으로 초기화
for i in range(1, n + 1):
    distance[i][i] = 0

# 회사 간 간선의 정보를 입력받기
for _ in range(m):
    # a에서 b까지의 거리 1
    a, b= map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

# 현재 간선 정보
def print_graph():
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            point = distance[a][b] if distance[a][b] != INF else -1
            print(point, end = " ")
        print()


print("before")
print_graph()
# X와 K를 입력받기
x, k = map(int, input().split())
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            old = distance[a][b]
            new = distance[a][i] + distance[i][b]
            distance[a][b] = min(old, new)

result = distance[1][k] + distance[k][x]

if result > 100:
    print(-1)
else:
    print(result)

print("after")
print_graph()