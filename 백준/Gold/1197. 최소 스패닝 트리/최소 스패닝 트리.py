from sys import stdin
input = stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
parent = list(range(V+1))

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

# 크루스칼 알고리즘 (MST의 가중치 합)
total_weight = 0
for u, v, weight in edges:
    # 사이클이 안생길 때
    if find(u) != find(v):
        union(u, v)
        total_weight += weight

print(total_weight)