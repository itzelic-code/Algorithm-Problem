def solution(N):
    answer = 0
    while N > 0:
		    # 2로 나누어 순간이동, 점프 별 건전지 추가
				# 만약 점프가 필요한 경우 +1
        answer += N % 2
        # 점프 후 2로 나눔
        N //= 2
    return answer