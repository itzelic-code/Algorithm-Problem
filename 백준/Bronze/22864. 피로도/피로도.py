import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())
tired = 0
work = 0

for _ in range(24):
    if M < A:
        break
    
    if tired + A <= M:
        tired += A
        work += B
    else:
        tired -= C
        if tired < 0:
            tired = 0
print(work)