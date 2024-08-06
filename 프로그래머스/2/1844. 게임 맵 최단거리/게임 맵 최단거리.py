from collections import deque

def solution(maps):
    # 이동할 수 있는 방향 (상, 하, 좌, 우)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rows, cols = len(maps), len(maps[0])

    # 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, 현재까지의 거리)

    while queue:
        x, y, distance = queue.popleft()

        # 목표 위치에 도착한 경우
        if x == rows - 1 and y == cols - 1:
            return distance

        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵의 범위를 벗어나지 않고, 이동할 수 있는 칸 (1)인 경우
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1:
                queue.append((nx, ny, distance + 1))
                # 방문한 칸은 0으로 변경하여 다시 방문하지 않게 함
                maps[nx][ny] = 0

    return -1  # 도달할 수 없는 경우