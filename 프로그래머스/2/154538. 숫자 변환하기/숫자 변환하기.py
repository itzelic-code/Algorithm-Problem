from collections import deque


def solution(x, y, n):
    # BFS를 위한 큐 초기화
    queue = deque([(x, 0)])  # (현재 숫자, 연산 횟수)
    visited = set()
    visited.add(x)

    while queue:
        current, steps = queue.popleft()

        # 목표 숫자에 도달한 경우
        if current == y:
            return steps

        # 가능한 연산
        next_values = [current + n, current * 2, current * 3]

        for next_value in next_values:
            if next_value <= y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, steps + 1))

    return -1  # 변환 불가능한 경우