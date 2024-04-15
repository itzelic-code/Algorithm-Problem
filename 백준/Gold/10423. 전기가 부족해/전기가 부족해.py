from sys import stdin
input = stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
power_plants = list(map(int, input().split()))
edges = []  # 간선 정보
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()
parent = [i for i in range(n+1)]
for p in power_plants:
    parent[p] = 0

result = 0

for edge in edges:
    cost, u, v = edge
    # 두 도시 중 하나라도 발전소가 있는 집합에 속함 & 사이클이 발생 X
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        result += cost

print(result)