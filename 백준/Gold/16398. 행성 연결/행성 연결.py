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

n = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

for i in range(1, n + 1):
    costs = list(map(int, input().split()))
    for j in range(n):
        if i != j:
            edges.append((costs[j], i, j+1))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
