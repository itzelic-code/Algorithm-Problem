from heapq import *

def solution(book_time):
	answer = 1
	
	# 예약시간 분단위로 변환&정렬
	book_time_min = []
	for s, e in book_time:
		start_min = int(s[:2]) * 60 + int(s[3:])
		end_min = int(e[:2]) * 60 + int(e[3:])
		book_time_min.append((start_min, end_min))
	book_time_min.sort()
	
	heap = []
	for s, e in book_time_min:
		# 객실이 존재하지 않으면 객실 할당
		if not heap:
			heappush(heap, e + 10)
			continue
		# 가장 빠른 종료 시간이 대실 시작 시간보다 같거나 빠르면 해당 객실 할당
		if heap[0] <= s: 
			heappop(heap)
		else: # 현재 객실 중 가장 빠른 종료 시간이 현재 대실 시작 시간보다 느리면 객실 추가
			answer += 1
		heappush(heap, e + 10)
	
	return answer