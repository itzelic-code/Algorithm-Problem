# 숫자의 표현

def solution(n):
    answer = 0
    
    # 1부터 n까지 순회
    for i in range(1, n+1):
        total = 0
        # i부터 n까지의 합 계산
        for j in range(i, n+1):
            total += j
            # 합이 n이면 1 증가
            if total == n:
                answer += 1
                break
            # 합이 n보다 커지면 종료
            elif total > n:
                break
    return answer