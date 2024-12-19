"""
* 메모리 : 33188KB
* 시간 : 848ms
* 사용된 개념 : 
--------------------------------------------------
* 접근 방법
1. 
	
--------------------------------------------------
"""

from heapq import *
from sys import stdin
input = stdin.readline

n = int(input())  # 사용자로부터 정수 N을 입력받음
heap = []  # 빈 힙 생성

for _ in range(n):
    numbers = list(map(int, input().split()))  # 한 줄에 해당하는 숫자들을 입력받음
    if not heap:  # 힙이 비어있는 경우, 처음 N개의 숫자를 힙에 삽입
        for number in numbers:
            heappush(heap, number)
    else:
        for number in numbers:
            if number > heap[0]:  # 새로운 숫자가 힙의 최소값보다 클 경우
                heappush(heap, number)  # 새 숫자를 힙에 삽입
                if len(heap) > n:  # 힙의 크기가 N보다 크면
                    heappop(heap)  # 힙의 최소값 제거

print(heap[0])  # 힙의 최소값 출력, 즉 N번째 큰 수
