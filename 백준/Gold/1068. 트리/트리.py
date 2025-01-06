
import sys
input = sys.stdin.readline

# DFS
def dfs(node, parents):
    parents[node] = -2  # 현재 노드 삭제
    for i in range(len(parents)):
        if node == parents[i]:  # 현재 노드가 부모인 경우,
            dfs(i, parents)   # 자식 노드를 재귀 탐색

# 입력
N = int(input())
parents = list(map(int, input().split()))
K = int(input())

# 노드 삭제
dfs(K, parents)

# 리프 노드 카운트
count = 0
for i in range(len(parents)):
    if parents[i] != -2 and i not in parents:
        count += 1

# 출력
print(count)