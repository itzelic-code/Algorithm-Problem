import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
X = int(input())

coprimes = []
for a in A:
    if gcd(a, X) == 1:
        coprimes.append(a)
        
print(sum(coprimes) / len(coprimes))