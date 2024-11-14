from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for visit in range(n):
        if visited[visit] == False:
            BFS(n, computers, visit, visited)
            answer += 1

    return answer


def BFS(n, computers, visit, visited):
    visited[visit] = True  # 방문
    queue = deque()
    queue.append(visit)

    while queue:
        visit = queue.pop()
        visited[visit] = True

        for i in range(n):
            if visited[i] == False and computers[i][visit] == 1 and i != visit:
                queue.append(i)
