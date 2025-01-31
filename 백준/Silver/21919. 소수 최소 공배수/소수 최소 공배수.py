# 21919 소수 최소 공배수
# https://www.acmicpc.net/problem/21919

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

MAX_A = 1000000
is_prime = [True] * (MAX_A + 1)
is_prime[0] = is_prime[1] = False 

# 에라토스테네스의 체
for i in range(2, int(MAX_A ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_A + 1, i):
            is_prime[j] = False 

# 소수 추출
primes_in_A = [num for num in A if is_prime[num]]

# 소수가 하나도 없을 경우 -1
if not primes_in_A:
    print(-1)
else:
    # 소수들의 최소공배수 계산
    answer = 1
    for prime in primes_in_A:
        answer *= prime
    print(answer)