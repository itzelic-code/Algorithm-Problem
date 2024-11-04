def solution(stones, k):
    start = 1
    end = max(stones)

    # 이진 탐색
    while start <= end:
        count = 0 # 연속으로 건널 수 있는 디딤돌 개수
        mid = (start + end) // 2
        for stone in stones:
            if (stone - mid) <= 0: # 현재 돌의 숫자가 mid 이하인 경우
                count += 1
                if count >= k: # 연속 디딤돌 개수가 k 이상인 경우
                    end = mid - 1
                    break
            else: # 건널 수 없는 경우
                count = 0
        else:
            start = mid + 1 # 더 낮은 mid 찾기
    return start