from heapq import *
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, graph):
    queue = []
    # 시작점 비용과 위치를 우선순위 큐에 삽입
    heappush(queue, (graph[0][0], 0, 0))
    distance = [[int(1e9)] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    
    while queue:
        dist, x, y = heappop(queue)
        if x == n-1 and y == n-1:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heappush(queue, (cost, nx, ny))
    return distance[n-1][n-1]

case = 0
while True:
    n = int(input().strip())
    if n == 0:
        break
    case += 1
    graph = [list(map(int, input().strip().split())) for _ in range(n)]
    result = dijkstra(n, graph)
    print(f"Problem {case}: {result}")
