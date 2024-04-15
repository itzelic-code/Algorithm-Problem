from heapq import *
from sys import stdin
input = stdin.readline

def dijkstra(start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        current_distance, current_node = heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance <= m and distance < distances[adjacent]:
                distances[adjacent] = distance
                heappush(queue, (distance, adjacent))
                
    return distances

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

max_items = 0
for i in range(1, n + 1):
    distances = dijkstra(i)
    item_count = sum(items[j] for j in range(1, n + 1) if distances[j] <= m)
    max_items = max(max_items, item_count)

print(max_items)