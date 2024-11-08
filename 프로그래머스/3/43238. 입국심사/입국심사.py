# 이분 탐색 문제 - O(MlogN)
def solution(n, times):
    left = 1
    right = max(times) * n  # 심사 시간의 최댓값
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time  # mid 시간 동안 심사한 사람 수
            if people >= n:  # n명 이상 심사했다면 종료
                break

        if people >= n:  # n명 이상 심사한 경우
            answer = mid
            right = mid - 1  # 탐색 범위 감소
        else:  # n명 미만 심사한 경우
            left = mid + 1  # 탐색 범위 증가

    return answer