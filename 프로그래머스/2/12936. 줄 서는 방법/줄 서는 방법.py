from math import factorial

def solution(n, k):
    answer = []
    arr = list(range(1, n + 1))
    k -= 1

    while n > 0:
        n -= 1
        f = factorial(n)
        idx = k // f
        answer.append(arr[idx])
        arr.pop(idx)
        k %= f

    return answer