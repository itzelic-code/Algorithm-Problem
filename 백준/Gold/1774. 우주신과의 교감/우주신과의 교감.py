import math
from sys import stdin
input = stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def calc_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

n, m = map(int, input().split())
locations = []
edges = []
parent = [0] * (n + 1)

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))
# 부모 => 자신
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((calc_distance(locations[i], locations[j]), i + 1, j + 1))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않을 때
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f"{result:.2f}")