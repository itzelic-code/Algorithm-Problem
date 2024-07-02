def solution(lottos, win_nums):
    answer = []
    count0 = lottos.count(0)
    correct = len(list(set(lottos) & set(win_nums)))
    # 최고 등수 = 7 - 0개수 - 맞은 개수
    # 최저 등수 = 7 - 맞은 개수
    answer.append(min(7 - (correct + count0), 6))
    answer.append(min(7 - correct, 6))

    return answer
