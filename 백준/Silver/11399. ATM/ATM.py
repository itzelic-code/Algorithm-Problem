import sys
input = sys.stdin.readline

N = int(input())
P = sorted(map(int, input().split()))

wait = 0
answer = 0
for i in P:
    wait += i
    answer += wait

print(answer)