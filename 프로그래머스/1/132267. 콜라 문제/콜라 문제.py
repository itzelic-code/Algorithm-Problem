def solution(a, b, n):
    answer = 0
    while (n >= a):
        p = a * (n // a)
        answer += p // a * b
        n = n - p + p // a * b
    return answer