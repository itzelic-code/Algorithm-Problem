def solution(brown, yellow):
    total = brown + yellow  # 전체 격자 개수
    
    # 전체 격자 개수 약수 찾기
    # 가로세로 길이가 1인 경우는 제외하기 위해 3부터 시작
    for i in range(3, int(total ** 0.5) + 1):
        if total % i == 0:
            j = total // i
            
            # 가로세로 합이 brown + 4가 되는 경우 찾아서 반환
            if 2 * (i + j) == brown + 4:
                return [j, i]
    
    return []