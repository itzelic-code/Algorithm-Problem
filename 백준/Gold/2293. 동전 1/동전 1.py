from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1) # 경우의 수
dp[0] = 1  # 동전 0개 사용

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])