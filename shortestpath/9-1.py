import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())

# 시작 노드번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 인덱스 값으로 바로 해당 노드 정보를 가져올 수 있게 크기가 n + 1인 리스트를 생성한다. 2차원 리스트
graph = [[] for i in range(n + 1)]

# 노드를 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화한다.
distance = [INF] * (n + 1)

# 간선의 값을 입력받는다
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b로가는 비용 = c
    graph[a].append((b, c))


# 방문하지 않은 노드 중 최단거리인 노드의 인덱스를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에서 시작노드까지의 값을 0으로 설정하고 방문기록을 True로 설정한다.
    distance[start] = 0
    visited[start] = True

    # 시작 노드의 간선정보들을 순회한다. j는 튜플형태이며 (목적지 노드, 간선의 값)의 형태로 이루어져있다.
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 노드의 개수 - 1만큼 순회한다. 시작 노드를 제외
    for i in range(n - 1):

        # 간선의 값이 가장 작은 즉, 최단거리 노드의 인덱스
        now = get_smallest_node()

        # 해당 노드를 방문처리
        visited[now] = True

        # 최단거리 노드에서 시작하는 간선들을 순회
        for j in graph[now]:

            # 시작점 ~ 현재노드 간선값 + 현재노드 ~ 목적지 간선값
            cost = distance[now] + j[1]

            # 기 등록된 최단거리 값과 비교했을 때 현재 노드에서 계산된 거리가 더 짧다면 이 값으로 최단거리 테이블을 갱신한다.
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])