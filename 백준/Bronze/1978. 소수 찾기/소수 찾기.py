import sys

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

N = int(input())
li = list(map(int, sys.stdin.readline().strip().split()))
count = 0

for num in li:
    if is_prime(num):
        count += 1
print(count)