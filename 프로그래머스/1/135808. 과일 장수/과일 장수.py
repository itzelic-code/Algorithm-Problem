def solution(k, m, score):
    cost = 0
    score.sort()
    for _ in range(len(score) // m):
        cost += list(score[-m:])[0] * m
        del score[-m:]
    return cost