import sys
import heapq

input = sys.stdin.readline

n = int(input())
sched = []

for _ in range(n):
    start, end = map(int, input().split())
    sched.append((start, end))

# 회의 시간표를 시작 시간 기준으로 정렬
sched.sort(key=lambda x: x[0])

# 최소 힙을 사용하여 가장 빨리 끝나는 회의 추적
min_heap = []
min_rooms = 0

for start, end in sched:
    # 현재 회의가 시작되기 전에 끝나는 회의들을 제거
    while min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    # 현재 회의를 힙에 추가
    heapq.heappush(min_heap, end)
    # 필요한 최소 회의실 개수 업데이트
    min_rooms = max(min_rooms, len(min_heap))

print(min_rooms)