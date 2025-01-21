T = int(input())
li = [int(input()) for _ in range(T)]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_num = int(n ** 0.5)
    for i in range(3, sqrt_num + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime(n):
    while not is_prime(n):
        n += 1
    return n

for n in li:
    print(find_prime(n))