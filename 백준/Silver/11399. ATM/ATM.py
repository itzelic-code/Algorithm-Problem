import sys, itertools
input = sys.stdin.readline

N = int(input())
P = sorted(map(int, input().split()))

wait = itertools.accumulate(P)
print(sum(wait))