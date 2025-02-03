def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n != 1

def is_palindrome(n) :
    n = str(n)
    return n[::-1] == n

n = int(input())

while True :
    if is_palindrome(n) and is_prime(n) :
        print(n)
        exit()
    n += 1