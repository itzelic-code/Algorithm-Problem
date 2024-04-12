from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = float('inf')


def dijikstra(start):
    dist = [INF] * len(graph)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, idx = heappop(q)
        if dist[idx] < cost:
            continue

        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))

    return dist

# 입력값 받기
n, m = map(int, input().split())
k = int(input())

#초기 설정
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 다익스트라
distance = dijikstra(k)
for i in range(1, n + 1):
    print(distance[i] if distance[i] != INF else "INF")