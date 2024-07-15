def solution(dartResult):
    n = ''  # 현재 숫자를 저장하는 변수
    score = []  # 각 라운드의 점수를 저장하는 리스트
    for i in dartResult:
        # 숫자인 경우
        if i.isnumeric():
            n += i  # 현재 숫자에 추가
        # S, D, T 인 경우
        elif i == 'S':
            n = int(n) ** 1  # 현재 숫자의 1제곱
            score.append(n)  # 점수 리스트에 추가
            n = ''  # 현재 숫자 초기화
        elif i == 'D':
            n = int(n) ** 2  # 현재 숫자의 2제곱
            score.append(n)  # 점수 리스트에 추가
            n = ''  # 현재 숫자 초기화
        elif i == 'T':
            n = int(n) ** 3  # 현재 숫자의 3제곱
            score.append(n)  # 점수 리스트에 추가
            n = ''  # 현재 숫자 초기화
        # * 인 경우
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2  # 이전 라운드 점수 2배
                score[-1] = score[-1] * 2  # 현재 라운드 점수 2배
            else:
                score[-1] = score[-1] * 2  # 현재 라운드 점수 2배
        # # 인 경우
        elif i == '#':
            score[-1] = score[-1] * -1  # 현재 라운드 점수 -1배
    
    return sum(score)  # 모든 라운드의 점수 합 반환