import math

def solution(n):
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        return int((sqrt + 1) ** 2)
    else:
        return -1
