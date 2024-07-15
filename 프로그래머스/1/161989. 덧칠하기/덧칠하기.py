def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작하는 지점
    for i in range(1, len(section)):
        # paint와 section의 간격 비교
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer