def solution(n, edge):
    adj = [[] for _ in range(n + 1)] # 인접 노드 리스트
    for v1, v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    visited = [0 for _ in range(n + 1)]
    visited[1] = 1
    queue = [1]
    
    while queue:
        current = queue.pop(0)
        for dest in adj[current]:
            if not visited[dest]:
                visited[dest] = visited[current] + 1 # 인덱스 번호 -> 노드 번호
                queue.append(dest)
        
    return visited.count(max(visited))