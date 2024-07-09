def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    return sum(range(start, end+1))
