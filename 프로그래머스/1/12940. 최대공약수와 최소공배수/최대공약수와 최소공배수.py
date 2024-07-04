def solution(n, m):
    a = n
    b = m
    while b != 0:
        a, b = b, a % b
    return a, n * m // a