import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())

for _ in range(T):
    li = list(map(int, input().split()))
    n = li[0]
    sum_ = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum_ += gcd(li[i], li[j])
    print(sum_)