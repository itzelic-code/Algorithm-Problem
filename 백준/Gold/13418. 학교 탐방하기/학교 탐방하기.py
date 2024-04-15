from sys import stdin
input = stdin.readline

def solution(N,edges):

    worstCourse, bestCourse = 0, N
    maxParent, minParent = [i for i in range(N+1)], [i for i in range(N+1)]
    
    def union(n1, n2, parent):
        n1 = find(n1, parent)
        n2 = find(n2, parent)
        parent[max(n1,n2)] = min(n1,n2)
    def find(n, parent):
        if n != parent[n]:
            parent[n] = find(parent[n],parent)
        return parent[n]
    
    for n1, n2, w in edges:
        # 최적의 코스
        if w == 1:
            n1 = find(n1,minParent)
            n2 = find(n2,minParent)
            if n1 != n2:
                bestCourse -= 1
                union(n1, n2, minParent)
        # 최악의 코스
        else:
            n1 = find(n1,maxParent)
            n2 = find(n2,maxParent)
            if n1 != n2:
                worstCourse += 1
                union(n1, n2, maxParent)

    return worstCourse**2 - bestCourse**2

N, M = map(int,input().split())
edges = [tuple(map(int,input().split())) for _ in range(M+1)]
result = solution(N,edges)
print(result)