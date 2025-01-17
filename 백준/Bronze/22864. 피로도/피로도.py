import sys

A, B, C, M = map(int, sys.stdin.readline().strip().split())
tired = 0
work = 0

if M < A:
    print(0)
else:
    for _ in range(24):
        if tired + A <= M:
            tired += A
            work += B
        else:
            tired = max(0, tired - C)
    print(work)