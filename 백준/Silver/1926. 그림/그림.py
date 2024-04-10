import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    visited[x][y] = True 
    count += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

pictures = 0
max_size = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            count = 0
            dfs(i, j)
            pictures += 1
            max_size = max(max_size, count)

print(pictures)
print(max_size)