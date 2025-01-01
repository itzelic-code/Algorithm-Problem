import sys
import math
input = sys.stdin.readline

n = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())
shirts_set = 0

for size in sizes:
    if size > 0:
        shirts_set += math.ceil(size / t)

print(shirts_set)
print(n // p, n % p)