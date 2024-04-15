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

n, m = map(int, input().split())
universities = input().split()
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    # 남-여 대학교 연결만!
    if universities[u-1] != universities[v-1]:
        edges.append((d, u, v))

edges.sort()
parent = [i for i in range(n+1)]
result = 0
count = 0

for edge in edges:
    cost, u, v = edge
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        result += cost
        count += 1
        if count == n-1:
	        break
	        
if count == n-1:
    print(result)
else:
    print(-1)  # 모든 대학교를 연결하지 못했을 때