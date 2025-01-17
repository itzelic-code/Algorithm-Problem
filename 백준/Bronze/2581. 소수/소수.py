def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())
primes = []

for num in range(M, N + 1):
    if is_prime(num):
        primes.append(num)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)