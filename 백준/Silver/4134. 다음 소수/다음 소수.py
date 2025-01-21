import sys
input = sys.stdin.readline

T = int(input())

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # n-1을 2^s * d 형태로 나타낸다.
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # 결정론적 Miller-Rabin 소수 판별법
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_prime(n):
    if n <= 2:
        return 2
    if n % 2 == 0: # n이 짝수인 경우
        n += 1  # 홀수로 변환
    while True:
        if is_prime(n):
            return n
        n += 2  # 홀수만 검사

for _ in range(T):
    n = int(input())
    print(find_prime(n))