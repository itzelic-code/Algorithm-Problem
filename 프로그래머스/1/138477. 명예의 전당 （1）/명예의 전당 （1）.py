def solution(k, score):
    answer = []
    input_ = []
    for i in score:
        # 만약 input_ 길이가 k보다 작으면 바로 input_에 삽입
        if len(input_) < k:
            input_.append(i)
        else:
            # 만약 input_의 최솟값이 새로운 값보다 작으면 갱신
            if min(input_) < i:
                input_.remove(min(input_))
                input_.append(i)
        # 명예의 전당 최솟값 저장
        answer.append(min(input_))
    return answer