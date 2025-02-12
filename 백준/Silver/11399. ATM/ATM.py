import sys, itertools

N = int(input())
print(sum(itertools.accumulate(sorted(map(int, sys.stdin.readline().split())))))