# 완전 탐색은 O(N^2)여서 타임 아웃
# 투 포인터 문제
def solution(gems):
    N = len(gems)
    answer = [0, N-1] # (시작, 끝) 포인터 인덱스
    kind = len(set(gems))  # 보석 종류 개수
    dic = {gems[0]: 1}  # 보석 종류 딕셔너리
    s, e = 0, 0  # 투 포인터

    while s < N and e < N:  # 두 포인터가 N보다 작을 때만 반복
        if len(dic) < kind:  # 보석 종류 부족한 경우
            e += 1  # 끝 포인터를 증가시켜 보석을 추가
            if e == N:  # 끝 포인터가 범위를 넘어가면 종료
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1  # 현재 보석 종류 추가 또는 카운트 증가
            
        else:  # 현재 보석 종류가 충분한 경우
            # 현재 구간의 길이가 더 짧으면 답 갱신
            if (e - s + 1) < (answer[1] - answer[0] + 1):
                answer = [s, e]  # 새로운 최적 구간으로 업데이트
            # 시작 포인터의 보석 종류를 제거
            if dic[gems[s]] == 1:  # 카운트가 1인 경우
                del dic[gems[s]]  # 해당 보석 종류 삭제
            else:
                dic[gems[s]] -= 1  # 카운트 감소
            s += 1  # 시작 포인터 증가

    answer[0] += 1
    answer[1] += 1
    return answer