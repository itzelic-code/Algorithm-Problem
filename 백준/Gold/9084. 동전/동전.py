from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]

    print(dp[M])