from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
dp = [0] * (M + 1)
for _ in range(N):
        m, v = map(int, input().split())
        for j in range(M, m-1, -1):
                dp[j] = max(dp[j], dp[j - m] + v)
print(dp[-1])