import sys
from collections import deque
 
input = sys.stdin.readline
# 입력 받기
m, n = map(int, input().split()) # m: 가로 길이, n: 세로 길이
map = [list(map(int,input().rstrip())) for _ in range(n)] # 미로 지도, 0은 이동 가능, 1은 벽
visited = [[-1]*m for _ in range(n)] # 방문 여부 및 해당 위치까지 도달하는데 부순 벽의 수 기록
dx = [0, 0, -1, 1] # x축 이동 방향 (상, 하)
dy = [1, -1, 0, 0] # y축 이동 방향 (우, 좌)
 
def bfs():
    q = deque()
    q.append((0, 0)) # 시작 위치 큐에 추가
    visited[0][0] = 0 # 시작 위치에서 부순 벽의 수는 0
    while q:
        x, y = q.popleft() # 큐에서 현재 위치 꺼내기
        if x == n-1 and y == m-1: # 목적지에 도착한 경우
            return visited[x][y] # 현재까지 부순 벽의 수 반환
 
        for i in range(4): # 상하좌우 네 방향으로의 이동 시도
            nx = x + dx[i] # 다음 x 위치
            ny = y + dy[i] # 다음 y 위치
            # 다음 위치가 미로 내부에 있고, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if map[nx][ny] == 0: # 이동하는 칸이 빈 방(벽이 없는 경우)
                    visited[nx][ny] = visited[x][y] # 벽을 부수지 않으므로, 부순 벽의 수 변화 없음
                    q.appendleft((nx, ny)) # 우선순위를 높여 바로 다음에 탐색하도록 큐의 앞쪽에 추가
                else: # 이동하는 칸에 벽이 있는 경우
                    visited[nx][ny] = visited[x][y] + 1 # 벽을 부수므로, 부순 벽의 수를 1 증가
                    q.append((nx, ny)) # 큐의 뒤쪽에 추가하여 나중에 탐색
print(bfs())