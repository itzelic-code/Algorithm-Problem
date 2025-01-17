def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(num ** 0.5)
    for i in range(3, sqrt_num + 1, 2):
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