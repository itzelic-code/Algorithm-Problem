def solve(n, x, y):
    if n == 0:
        return 0
    half = 2**(n-1)
    if x < half:
        if y < half:
            return solve(n-1, x, y)
        else:
            return half*half + solve(n-1, x, y-half)
    else:
        if y < half:
            return 2*half*half + solve(n-1, x-half, y)
        else:
            return 3*half*half + solve(n-1, x-half, y-half)

N, r, c = map(int, input().split())
print(solve(N, r, c))
