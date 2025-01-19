from math import gcd, sqrt
n = int(input())
lst = []

if n == 2:
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)


if n == 3:
    a, b, c = map(int, input().split())
    gcd_ = gcd(gcd(a, b), c)

for i in range(1, int(sqrt(gcd_)) + 1):
    if gcd_ % i == 0:
        lst.append(i)
        if i**2 != gcd_:
            lst.append(gcd_ // i)

lst.sort()

for num in lst:
    print(num)