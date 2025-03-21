import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(' '.join(str(n) for n in sorted(A+B)))