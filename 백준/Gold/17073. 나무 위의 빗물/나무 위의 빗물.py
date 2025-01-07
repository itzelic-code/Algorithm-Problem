from sys import stdin
from collections import defaultdict

N, W = list(map(int, stdin.readline().split()))
tree = defaultdict(list)
for i in range(N-1):
    u, v = list(map(int, stdin.readline().split()))
    tree[u].append(v)
    tree[v].append(u)

leaf_count = 0
for root, nodes in tree.items():
    if root!=1 and len(nodes)==1:
        leaf_count+=1

print(round(W/leaf_count, 10))