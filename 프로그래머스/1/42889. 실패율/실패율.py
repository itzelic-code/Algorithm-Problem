def solution(N, stages):
    answer = []
    
    # 1. 각 스테이지별 도달한 사람 수와 클리어하지 못한 사람 수 계산
    stage_info = [0] * (N + 1)
    for stage in stages:
        if stage <= N:
            stage_info[stage] += 1
    
    # 2. 각 스테이지별 실패율 계산
    fail_rates = []
    total = len(stages)
    for i in range(1, N + 1):
        if total == 0:
            fail_rate = 0
        else:
            fail_rate = stage_info[i] / total
        fail_rates.append((i, fail_rate))
        total -= stage_info[i]
    
    # 3. 실패율을 기준으로 내림차순 정렬
    fail_rates.sort(key=lambda x: x[1], reverse=True)
    
    # 4. 정렬된 스테이지 번호를 answer에 추가
    for stage, _ in fail_rates:
        answer.append(stage)
    
    return answer