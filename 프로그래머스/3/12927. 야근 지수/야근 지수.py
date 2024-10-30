import heapq

def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-work for work in works]
    heapq.heapify(works)

    while n > 0:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1

    return sum(work ** 2 for work in works)