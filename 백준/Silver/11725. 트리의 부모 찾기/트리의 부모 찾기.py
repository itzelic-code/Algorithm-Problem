import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
vertices = [[0] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    # 두 정점의 Linked List에 각각 저장
    vertices[a].append(b)
    vertices[b].append(a)

parent[1] = 0
q = deque()
q.append(1)

while q:
    current = q.popleft()
    for v in vertices[current]:
        # 이미 parent에 기록된 것은 부모가 있음
        # 해당 정점과 연결된 것들은 모두 자식
        if parent[v] == 0:
            parent[v] = current
            q.append(v)

print('\n'.join(map(str, parent[2:])))