from heapq import *
from sys import stdin
input = stdin.readline

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distances[start] = 0
    while heap:
        current_distance, current_vertex = heappop(heap)
        if distances[current_vertex] < current_distance:
            continue
        for adj, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heappush(heap, (distance, adj))
                
T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distances = [float('inf')] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))  # b에서 a로 가는 시간 s
    dijkstra(c)
    
    infected = 0
    last_time = 0
    for distance in distances:
        if distance != float('inf'):
            infected += 1
            if distance > last_time:
                last_time = distance
    print(infected, last_time)
