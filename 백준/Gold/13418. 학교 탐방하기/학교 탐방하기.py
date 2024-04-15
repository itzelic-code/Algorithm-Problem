from sys import stdin

def solution(N,edges):

    worstCourse, bestCourse = 0, N
    maxParent, minParent = [i for i in range(N+1)], [i for i in range(N+1)]

    # [1] Union & Find
    def union(n1, n2, parent):
        n1 = find(n1, parent)
        n2 = find(n2, parent)
        parent[max(n1,n2)] = min(n1,n2)
    def find(n, parent):
        if n != parent[n]:
            parent[n] = find(parent[n],parent)
        return parent[n]
    
    # [2] 최적, 최악의 코스 찾기
    for n1, n2, w in edges:
        # [2-1] 최적의 코스
        if w == 1:
            n1 = find(n1,minParent)
            n2 = find(n2,minParent)
            if n1 != n2:
                bestCourse -= 1
                union(n1, n2, minParent)
        # [2-2] 최악의 코스
        else:
            n1 = find(n1,maxParent)
            n2 = find(n2,maxParent)
            if n1 != n2:
                worstCourse += 1
                union(n1, n2, maxParent)

    return worstCourse**2 - bestCourse**2

# input
N, M = map(int,stdin.readline().split())
edges = [tuple(map(int,stdin.readline().split())) for _ in range(M+1)]

# result
result = solution(N,edges)
print(result)