# 플로이드 워셜 알고리즘

INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 거리는 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 수행된 결과를 출력
def printer():
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
            if graph[a][b] == INF:
                print("INFINITY", end = " ")
            else:
                print(graph[a][b], end = " ")
        print()

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 기존의 a와 b의 간선 값
            old = graph[a][b]
            # a에서 k를 경유해 b로 가는 경로의 값
            new = graph[a][k] + graph[k][b]
            graph[a][b] = min(old, new)


printer()