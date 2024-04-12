import heapq
from sys import stdin

input = stdin.readline
INF = int(1e9) # 정점 거리 초기화를 위한 무한대 값

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)] # 도시 정보

# 버스 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가는 최단 경로는 0
    distance[start] = 0
    while q: # 큐가 비어있지 않을 때
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드
        if distance[now] < dist: # 이미 처리된 노드면 패쓰
            continue
        for i in graph[now]: # 현재 노드랑 인접한 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 비용이 더 저렴할 때
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])