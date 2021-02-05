# 전보
# 문제 - 전보를 받을 수 있는 도시의 개수와 전달에 필요한 시간
# 전보를 받을 수 있는 도시의 개수 = 경로가 무한대 값이 아닌 도시의 개수
# 전달에 필요한 시간 = ??

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# n, m, start 각각 도시의 개수, 통로의 개수, 출발도시
n, m, start = map(int, input().split())

# 경로정보를 저장할 변수 생성
graph = [[] * (n + 1)]

# 최단거리를 갱신할 변수 생성
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(1, m + 1):
    x, y, z = map(int, input().split())
    graph[x].append(y, z)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고 큐에 삽입한다.
    heapq.heappush(q, (0, start))
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보를 꺼낸다
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappop(q, (cost, i[0]))


dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)


# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)

