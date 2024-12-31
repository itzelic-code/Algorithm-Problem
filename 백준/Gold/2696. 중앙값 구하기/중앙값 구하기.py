import sys
import heapq
input = sys.stdin.readline

def solution(arr):
    mid = arr[0] # 중앙값 초기화
    small = [] # 중앙값보다 작은 값을 저장하는 힙
    big = [] # 중앙값보다 큰 값을 저장하는 힙
    answer = [mid] # 중앙값들을 저장할 리스트

    # 집합을 mid보다 작은 부분(big)과 작은 부분(small)으로
    # 나누어서 중앙값을 계산한다.
    for idx, val in enumerate(arr[1:], 1):
        # 중앙값보다 큰 값은 big에 추가
        if val > mid:
            heapq.heappush(big, val)
        else: # 중앙값보다 작은 값은 small에 추가 (최대힙이므로 음수 저장)
            heapq.heappush(small, (-val, val))

         # 짝수(홀수)번째 값을 처리할 때마다 중앙갑 업데이트
        if idx % 2 == 0:
            # big 힙의 크기가 더 크면 small 힙에 추가
            if len(small) < len(big):
                # 현재 중앙값을 small힙에 추가
                heapq.heappush(small, (-mid, mid))
                # big 힙의 최솟값을 중앙값으로
                mid = heapq.heappop(big)

            # small 힙의 크기가 더 크면 big 힙에 추가
            elif len(small) > len(big):
                # 현재 중앙값을 big힙에 추가
                heapq.heappush(big, mid)
                # small힙의 최댓값을 중앙값으로
                mid = heapq.heappop(small)[1]
            answer.append(mid) # 갱신된 중앙값 저장
    print(len(answer)) # 중앙값 개수 출력

    for i in range(len(answer)):
        if i != 0 and (i + 1) % 10 == 1:
            print() # 10개씩 출력 위한 줄바꿈
        print(answer[i], end=' ') # 중앙값 출력
    print()


# 테스트 케이스 수 T 만큼 동작
T = int(input().rstrip())
for _ in range(T):
    M = int(input().rstrip())
    arr = []

    for _ in range(M // 10 + (M % 10 != 0)):
            arr.extend(list(map(int, input().rstrip().split())))
    
    solution(arr)