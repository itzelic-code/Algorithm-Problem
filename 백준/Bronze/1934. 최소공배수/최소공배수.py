from math import gcd

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))