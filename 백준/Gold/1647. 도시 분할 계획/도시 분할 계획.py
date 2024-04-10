from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
parent = list(range(N+1))

def find(x):
    if parent[x] != x:
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
total_cost = 0
max_cost = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        max_cost = max(max_cost, cost)

# 최대 유지비 제거
print(total_cost - max_cost)