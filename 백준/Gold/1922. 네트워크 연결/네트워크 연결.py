from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = list(range(N+1))

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
total_cost = 0
for u, v, cost in edges:
    # 사이클이 안생길 때
    if find(u) != find(v):
        union(u, v)
        total_cost += cost

print(total_cost)