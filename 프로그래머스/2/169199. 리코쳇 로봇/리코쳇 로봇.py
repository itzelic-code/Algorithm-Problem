from collections import *

# 상하좌우 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def solution(board):
    answer = 0
    N = len(board)  # board 가로 길이
    M = len(board[0])  # board 세로 길이
    q = deque()  # 큐 초기화
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]  # 거리 배열 초기화

    # 1. 로봇(R)의 시작 위치를 찾아서 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i, j, 0))  # 시작 위치와 이동횟수 0 큐에 추가
                dist[i][j] = 0  # 시작 위치의 거리 초기화
        if q:
            break

    # 2. BFS 탐색 시작
    while q:
        x, y, count = q.popleft()  # 큐에서 현재 위치, 이동 횟수 꺼내기

        # 3. 목표 지점(G)에 도착한 경우 이동 횟수 반환 [결과 반환]
        if board[x][y] == 'G':
            return count

        # 4. 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            nx = x
            ny = y

            # 5. 해당 방향으로 이동 가능한 위치 찾기
            while (0 <= nx + dx[i] < N and  # x 좌표가 범위를 벗어나지 않으면서
                   0 <= ny + dy[i] < M and  # y 좌표가 범위를 벗어나지 않으면서
                   board[nx + dx[i]][ny + dy[i]] != 'D'):  # 다음 위치가 벽이 아닌 경우
                nx += dx[i]  # 좌표 이동
                ny += dy[i]

            # 6. 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우
            if dist[nx][ny] > count + 1:
                dist[nx][ny] = count + 1  # 거리 갱신
                q.append((nx, ny, count + 1))  # 새로운 위치와 이동 횟수 큐에 추가

    # 7. 목표 지점에 도착할 수 없는 경우 -1 반환 [결과 반환]
    return -1