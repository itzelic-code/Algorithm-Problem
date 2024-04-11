import math
from sys import stdin
input = stdin.readline

# 좌표간 거리
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

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
stars = [tuple(map(float, input().split())) for _ in range(n)] # 별의 좌표
edges = []

# 별 사이 거리 => 간선
for i in range(n):
    for j in range(i+1, n):
        edges.append((distance(stars[i], stars[j]), i, j))
edges.sort()

parent = [i for i in range(n)]

minimal_cost = 0 # 최소 비용
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않을 때
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        minimal_cost += cost

print("%.2f" % minimal_cost)