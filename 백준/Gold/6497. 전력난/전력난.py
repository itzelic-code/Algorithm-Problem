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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: break
    roads = []
    total_cost = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        roads.append((z, x, y))
        total_cost += z
        
    roads.sort()
    parent = [i for i in range(m)]

    mst_cost = 0
    for road in roads:
        cost, a, b = road
        # 사이클이 발생하지 않을 때
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst_cost += cost

    print(total_cost - mst_cost)