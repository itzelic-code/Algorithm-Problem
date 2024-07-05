def solution(s):
    answer = [int(x) for x in s.split()]
    return str(min(answer)) + ' ' + str(max(answer))