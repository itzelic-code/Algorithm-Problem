import heapq
import sys

def dijkstra(start, graph):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node]:
            distance = current_distance + new_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])

    return distances

input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))
    reverse_graph[B].append((A, T))

# X에서 각 지점으로 가는 최단 거리 계산
to_X = dijkstra(X, reverse_graph)

# 각 지점에서 X로 가는 최단 거리 계산
from_X = dijkstra(X, graph)

# 가는 시간과 오는 시간의 합이 최대가 되는 값을 찾음
max_time = max(from_X[i] + to_X[i] for i in range(1, N + 1))

print(max_time)