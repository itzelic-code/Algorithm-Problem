from collections import deque

n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    friends = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    if campus[nx][ny] == 'P':
                        friends += 1
                    queue.append((nx, ny))
    return friends

# I의 위치 찾기
start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start_x, start_y = i, j

result = bfs(start_x, start_y)
print(result if result != 0 else "TT")
